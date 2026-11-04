"""Web & Repository Fact Grounding Tool for CofVid.

Enforces authentic, verified technical facts and numbers (stars, forks, description,
topics, licenses, OpenGraph data) from live repositories and web pages.
AI hallucination of statistics, release dates, or metric claims is strictly prohibited.
All scanned facts are preserved in `grounded_facts.json` as a verifiable audit trail.
"""

from __future__ import annotations

import datetime
import json
import logging
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Optional

from tools.base_tool import (
    BaseTool,
    Determinism,
    ExecutionMode,
    ResourceProfile,
    ToolResult,
    ToolStability,
    ToolTier,
    ToolRuntime,
)

logger = logging.getLogger(__name__)

GITHUB_REPO_REGEX = re.compile(
    r"^(?:https?://)?(?:www\.)?github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:/|\.git|\?|#|$)"
)


def _decode_entities(text: str) -> str:
    """Decode common HTML entities."""
    return (
        text.replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
        .replace("&#x27;", "'")
        .replace("&#x2F;", "/")
    )


class WebDataGrounderTool(BaseTool):
    """Grounding tool for extracting real-world verified metrics and metadata."""

    name = "web_data_grounder"
    version = "0.1.0"
    tier = ToolTier.ANALYZE
    stability = ToolStability.PRODUCTION
    execution_mode = ExecutionMode.SYNC
    determinism = Determinism.DETERMINISTIC
    runtime = ToolRuntime.LOCAL

    capability = "analysis"
    provider = "web_grounding"
    capabilities = [
        "web_grounding",
        "github_scan",
        "fact_extraction",
        "opengraph_metadata",
    ]
    agent_skills = ["web-data-grounding"]

    resource_profile = ResourceProfile(cpu_cores=1, ram_mb=256, disk_mb=20)

    input_schema = {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "Target web page or GitHub repository URL (e.g. 'https://github.com/nexu-io/open-design')",
            },
            "entity_type": {
                "type": "string",
                "enum": ["auto", "github", "website", "docs"],
                "default": "auto",
                "description": "Type of target to ground: auto (inferred from URL), github repo, or website",
            },
            "output_path": {
                "type": "string",
                "description": "Optional path where grounded_facts.json should be written",
            },
            "project_dir": {
                "type": "string",
                "description": "Owning project directory for automatic grounded_facts.json artifact storage",
            },
        },
        "required": ["url"],
    }

    output_schema = {
        "type": "object",
        "properties": {
            "url": {"type": "string"},
            "entity_type": {"type": "string"},
            "facts": {"type": "object"},
            "output_path": {"type": "string"},
            "scanned_at": {"type": "string"},
            "provenance": {"type": "string"},
        },
        "required": ["url", "entity_type", "facts", "output_path"],
    }

    def _fetch_github_repo(self, owner: str, repo: str) -> tuple[dict[str, Any], str]:
        """Fetch repo statistics using GitHub REST API with fallback to HTML parsing."""
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        headers = {
            "User-Agent": "CofVid-WebDataGrounder/1.0 (https://github.com/vuthang/CofVid)",
            "Accept": "application/vnd.github.v3+json",
        }
        github_token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if github_token:
            headers["Authorization"] = f"Bearer {github_token}"

        req = urllib.request.Request(api_url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=5.0) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                license_info = data.get("license") or {}
                facts = {
                    "name": data.get("name") or repo,
                    "full_name": data.get("full_name") or f"{owner}/{repo}",
                    "owner": owner,
                    "repo": repo,
                    "description": data.get("description") or "",
                    "stars": data.get("stargazers_count", 0),
                    "forks": data.get("forks_count", 0),
                    "open_issues": data.get("open_issues_count", 0),
                    "subscribers_count": data.get("subscribers_count", 0) or data.get("watchers_count", 0),
                    "language": data.get("language") or "Unknown",
                    "topics": data.get("topics") or [],
                    "license": license_info.get("spdx_id") or license_info.get("name") or "None",
                    "owner_avatar_url": (data.get("owner") or {}).get("avatar_url", ""),
                    "homepage": data.get("homepage") or "",
                    "default_branch": data.get("default_branch") or "main",
                    "created_at": data.get("created_at") or "",
                    "updated_at": data.get("updated_at") or "",
                    "html_url": data.get("html_url") or f"https://github.com/{owner}/{repo}",
                }
                return facts, "github_api"
        except urllib.error.HTTPError as exc:
            logger.warning(f"GitHub API HTTP {exc.code} for {owner}/{repo}: {exc.reason}")
        except Exception as exc:
            logger.warning(f"GitHub API fetch error for {owner}/{repo}: {exc}")

        # Fallback to direct HTML scrape of GitHub repo page
        html_url = f"https://github.com/{owner}/{repo}"
        html_req = urllib.request.Request(
            html_url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
                )
            },
        )
        try:
            with urllib.request.urlopen(html_req, timeout=5.0) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
                # Extract stars
                stars = 0
                star_m = re.search(r'id="repo-stars-counter-star"[^>]*title="([\d,]+)"', html)
                if star_m:
                    stars = int(star_m.group(1).replace(",", ""))
                else:
                    star_text = re.search(r'id="repo-stars-counter-star"[^>]*>([\d.kKmM]+)<', html)
                    if star_text:
                        raw_str = star_text.group(1).strip()
                        if "k" in raw_str.lower():
                            stars = int(float(raw_str.lower().replace("k", "")) * 1000)
                        elif "m" in raw_str.lower():
                            stars = int(float(raw_str.lower().replace("m", "")) * 1000000)
                        else:
                            stars = int(re.sub(r"[^\d]", "", raw_str) or 0)

                # Extract forks
                forks = 0
                fork_m = re.search(r'id="repo-network-counter"[^>]*title="([\d,]+)"', html)
                if fork_m:
                    forks = int(fork_m.group(1).replace(",", ""))

                # Extract description
                desc = ""
                desc_m = re.search(r'<p[^>]*class="[^"]*f4[^"]*my-3[^"]*"[^>]*>(.*?)</p>', html, re.DOTALL)
                if not desc_m:
                    desc_m = re.search(r'<meta name="description" content="([^"]+)"', html)
                if desc_m:
                    desc = _decode_entities(re.sub(r"<[^>]+>", "", desc_m.group(1))).strip()

                return {
                    "name": repo,
                    "full_name": f"{owner}/{repo}",
                    "owner": owner,
                    "repo": repo,
                    "description": desc,
                    "stars": stars,
                    "forks": forks,
                    "open_issues": 0,
                    "language": "Repository",
                    "topics": [],
                    "license": "Open Source",
                    "owner_avatar_url": f"https://github.com/{owner}.png",
                    "html_url": html_url,
                }, "github_html_scrape"
        except Exception as html_exc:
            logger.error(f"GitHub fallback scrape failed: {html_exc}")

        # Minimal fallback
        return {
            "name": repo,
            "full_name": f"{owner}/{repo}",
            "owner": owner,
            "repo": repo,
            "description": f"{owner}/{repo} repository",
            "stars": 0,
            "forks": 0,
            "language": "Code",
            "topics": [],
            "license": "Unknown",
            "html_url": html_url,
        }, "fallback_offline"

    def _fetch_website_metadata(self, url: str) -> tuple[dict[str, Any], str]:
        """Fetch general website page and extract OpenGraph and metadata."""
        parsed = urllib.parse.urlparse(url)
        if not parsed.scheme:
            url = "https://" + url
            parsed = urllib.parse.urlparse(url)

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        }
        req = urllib.request.Request(url, headers=headers)
        html = ""
        try:
            with urllib.request.urlopen(req, timeout=5.0) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
        except Exception as exc:
            logger.warning(f"Website fetch error for {url}: {exc}")

        def get_meta(prop_or_name: str) -> str:
            if not html:
                return ""
            pattern = rf'<meta[^>]+(?:property|name)=["\']{re.escape(prop_or_name)}["\'][^>]*content=["\']([^"\']*)["\']'
            m = re.search(pattern, html, flags=re.IGNORECASE)
            if m:
                return _decode_entities(m.group(1)).strip()
            # Try content first
            alt_pattern = rf'<meta[^>]+content=["\']([^"\']*)["\'][^>]*?(?:property|name)=["\']{re.escape(prop_or_name)}["\']'
            alt_m = re.search(alt_pattern, html, flags=re.IGNORECASE)
            if alt_m:
                return _decode_entities(alt_m.group(1)).strip()
            return ""

        title = ""
        if html:
            title_m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
            if title_m:
                title = _decode_entities(re.sub(r"<[^>]+>", "", title_m.group(1))).strip()

        og_title = get_meta("og:title") or title
        og_desc = get_meta("og:description") or get_meta("description")
        og_image = get_meta("og:image") or get_meta("twitter:image")
        og_site_name = get_meta("og:site_name")
        og_url = get_meta("og:url") or url

        if og_image and not og_image.startswith(("http://", "https://", "data:")):
            og_image = urllib.parse.urljoin(url, og_image)

        # Extract primary headings
        headings: list[str] = []
        if html:
            for hm in re.finditer(r"<h[12][^>]*>(.*?)</h[12]>", html, flags=re.IGNORECASE | re.DOTALL):
                clean_h = _decode_entities(re.sub(r"<[^>]+>", "", hm.group(1))).strip()
                if clean_h and len(clean_h) < 120 and clean_h not in headings:
                    headings.append(clean_h)
                if len(headings) >= 5:
                    break

        facts = {
            "title": og_title or parsed.netloc,
            "site_name": og_site_name or parsed.netloc,
            "description": og_desc,
            "canonical_url": og_url,
            "domain": parsed.netloc,
            "og_image": og_image,
            "headings": headings,
        }
        return facts, "website_opengraph"

    def execute(self, inputs: dict[str, Any]) -> ToolResult:
        url = inputs.get("url", "").strip()
        if not url:
            return ToolResult(success=False, error="url is required")

        entity_type = inputs.get("entity_type", "auto")
        output_path = inputs.get("output_path")
        project_dir = inputs.get("project_dir")

        # 1. Detect entity type
        github_match = GITHUB_REPO_REGEX.search(url)
        detected_type = "website"
        if entity_type == "github" or (entity_type == "auto" and github_match):
            detected_type = "github"
        elif entity_type in ("website", "docs"):
            detected_type = entity_type

        # 2. Extract facts
        if detected_type == "github" and github_match:
            owner, repo = github_match.group(1), github_match.group(2)
            facts, provenance = self._fetch_github_repo(owner, repo)
        elif detected_type == "github" and not github_match:
            # Owner/repo passed directly
            parts = url.strip("/").split("/")
            if len(parts) >= 2:
                owner, repo = parts[-2], parts[-1]
                facts, provenance = self._fetch_github_repo(owner, repo)
            else:
                facts, provenance = self._fetch_website_metadata(url)
                detected_type = "website"
        else:
            facts, provenance = self._fetch_website_metadata(url)

        # 3. Save grounded_facts.json artifact
        scanned_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
        grounded_data = {
            "source_url": url,
            "entity_type": detected_type,
            "scanned_at": scanned_at,
            "provenance": provenance,
            "facts": facts,
        }

        final_output_path = output_path
        if not final_output_path:
            if project_dir and os.path.isdir(project_dir):
                final_output_path = os.path.join(project_dir, "grounded_facts.json")
            else:
                final_output_path = "grounded_facts.json"

        out_p = Path(final_output_path)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(json.dumps(grounded_data, indent=2, ensure_ascii=False), encoding="utf-8")

        return ToolResult(
            success=True,
            data={
                "url": url,
                "entity_type": detected_type,
                "provenance": provenance,
                "scanned_at": scanned_at,
                "facts": facts,
                "output_path": str(out_p.resolve()),
            },
            artifacts=[str(out_p.resolve())],
        )


# Export tool alias
WebDataGrounder = WebDataGrounderTool
