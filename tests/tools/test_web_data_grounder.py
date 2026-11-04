"""Unit tests for WebDataGrounderTool (Web & Repo Fact Grounding)."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from tools.analysis.web_data_grounder import WebDataGrounderTool
from tools.base_tool import ToolRuntime, ToolStatus, ToolTier
from tools.graphics.open_design_tool import OpenDesignTool


@pytest.fixture
def grounder() -> WebDataGrounderTool:
    return WebDataGrounderTool()


def test_web_grounder_contract(grounder: WebDataGrounderTool):
    """Verify tool identity and capabilities contract."""
    assert grounder.name == "web_data_grounder"
    assert grounder.capability == "analysis"
    assert grounder.provider == "web_grounding"
    assert grounder.runtime == ToolRuntime.LOCAL
    assert grounder.tier == ToolTier.ANALYZE
    assert grounder.get_status() == ToolStatus.AVAILABLE
    assert "web_grounding" in grounder.capabilities
    assert "github_scan" in grounder.capabilities
    assert "fact_extraction" in grounder.capabilities


def test_github_repo_grounding(grounder: WebDataGrounderTool, tmp_path: Path):
    """Verify GitHub API fact extraction and artifact generation."""
    mock_gh_data = {
        "name": "open-design",
        "full_name": "nexu-io/open-design",
        "description": "Anti-AI Slop open source editorial design systems",
        "stargazers_count": 1420,
        "forks_count": 128,
        "open_issues_count": 9,
        "language": "TypeScript",
        "topics": ["design-systems", "typography", "editorial", "video"],
        "license": {"spdx_id": "MIT", "name": "MIT License"},
        "owner": {"avatar_url": "https://avatars.githubusercontent.com/u/12345"},
        "created_at": "2024-01-15T08:00:00Z",
        "updated_at": "2026-10-30T10:00:00Z",
        "html_url": "https://github.com/nexu-io/open-design",
    }

    mock_resp = MagicMock()
    mock_resp.status = 200
    mock_resp.read.return_value = json.dumps(mock_gh_data).encode("utf-8")
    mock_resp.__enter__.return_value = mock_resp

    out_file = tmp_path / "grounded_facts.json"

    with patch("urllib.request.urlopen", return_value=mock_resp):
        result = grounder.execute({
            "url": "https://github.com/nexu-io/open-design",
            "output_path": str(out_file),
        })

    assert result.success is True
    assert result.data["entity_type"] == "github"
    assert result.data["provenance"] == "github_api"
    facts = result.data["facts"]
    assert facts["name"] == "open-design"
    assert facts["stars"] == 1420
    assert facts["forks"] == 128
    assert facts["open_issues"] == 9
    assert facts["language"] == "TypeScript"
    assert facts["license"] == "MIT"

    # Verify JSON artifact written to disk
    assert out_file.is_file()
    saved = json.loads(out_file.read_text(encoding="utf-8"))
    assert saved["source_url"] == "https://github.com/nexu-io/open-design"
    assert saved["facts"]["stars"] == 1420


def test_website_opengraph_grounding(grounder: WebDataGrounderTool, tmp_path: Path):
    """Verify general website OpenGraph metadata extraction."""
    mock_html = """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Next-Gen Video Synthesis | CofVid Studio</title>
        <meta property="og:title" content="Next-Gen Video Synthesis">
        <meta property="og:description" content="Instruction-driven video production architecture for autonomous agents.">
        <meta property="og:image" content="https://cofvid.dev/assets/social-banner.png">
        <meta property="og:site_name" content="CofVid Studio">
        <meta property="og:url" content="https://cofvid.dev">
      </head>
      <body>
        <h1>Autonomous Media Engineering</h1>
        <h2>Deterministic Rendering</h2>
      </body>
    </html>
    """

    mock_resp = MagicMock()
    mock_resp.status = 200
    mock_resp.read.return_value = mock_html.encode("utf-8")
    mock_resp.__enter__.return_value = mock_resp

    out_file = tmp_path / "website_facts.json"

    with patch("urllib.request.urlopen", return_value=mock_resp):
        result = grounder.execute({
            "url": "https://cofvid.dev",
            "entity_type": "website",
            "output_path": str(out_file),
        })

    assert result.success is True
    assert result.data["entity_type"] == "website"
    assert result.data["provenance"] == "website_opengraph"
    facts = result.data["facts"]
    assert facts["title"] == "Next-Gen Video Synthesis"
    assert "Instruction-driven" in facts["description"]
    assert facts["og_image"] == "https://cofvid.dev/assets/social-banner.png"
    assert "Autonomous Media Engineering" in facts["headings"]


def test_auto_entity_type_detection(grounder: WebDataGrounderTool):
    """Verify entity_type auto detection based on target URL."""
    # GitHub URL
    with patch.object(grounder, "_fetch_github_repo", return_value=({"stars": 50000}, "mock")):
        res_gh = grounder.execute({"url": "https://github.com/torvalds/linux"})
        assert res_gh.data["entity_type"] == "github"

    # Website URL
    with patch.object(grounder, "_fetch_website_metadata", return_value=({"title": "Test"}, "mock")):
        res_web = grounder.execute({"url": "https://en.wikipedia.org/wiki/Linux"})
        assert res_web.data["entity_type"] == "website"


def test_grounded_facts_integration_with_open_design(grounder: WebDataGrounderTool, tmp_path: Path):
    """Verify grounded facts directly feed open_design_tool without AI fabrication."""
    mock_gh_data = {
        "name": "react",
        "full_name": "facebook/react",
        "description": "The library for web and native user interfaces",
        "stargazers_count": 225000,
        "forks_count": 45000,
        "open_issues_count": 1200,
        "language": "JavaScript",
        "license": {"spdx_id": "MIT"},
    }
    mock_resp = MagicMock()
    mock_resp.read.return_value = json.dumps(mock_gh_data).encode("utf-8")
    mock_resp.__enter__.return_value = mock_resp

    with patch("urllib.request.urlopen", return_value=mock_resp):
        grounding_res = grounder.execute({
            "url": "https://github.com/facebook/react",
            "output_path": str(tmp_path / "grounded_facts.json"),
        })

    facts = grounding_res.data["facts"]
    stars_str = f"{facts['stars']:,}"  # '225,000'

    # Feed verified numbers into Open Design Stat Callout
    od = OpenDesignTool()
    card_res = od.execute({
        "component_type": "stat_callout",
        "theme_id": "dark-data",
        "props": {
            "brand_slug": "react",
            "kicker": "VERIFIED GITHUB METRIC",
            "stat": stars_str,
            "title": f"Stars on {facts['name'].title()}",
            "body": facts["description"],
            "meta": f"SOURCE: {facts['license']} // GROUNDED VIA WEB_DATA_GROUNDER",
        },
    })

    assert card_res.success is True
    dom = card_res.data["dom_snippet"]
    assert "225,000" in dom
    assert "od-brand-icon" in dom
    assert "<svg" in dom
    assert "VERIFIED GITHUB METRIC" in dom
