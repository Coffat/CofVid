---
name: web-data-grounding
description: >
  Live web and GitHub repository fact grounding tool for CofVid. Extracts verified
  metrics, stars, forks, release dates, licenses, and OpenGraph metadata to eliminate
  factual AI hallucination in scripts and graphic cards. Produces grounded_facts.json.
metadata: { "tags": "analysis, grounding, github, metrics, opengraph, facts, audit" }
---

# Web & Repo Fact Grounding — Verified Documentary Evidence

`web_data_grounder` is CofVid's audit and fact-extraction engine. It connects to live GitHub repositories and website URLs to harvest **concrete, verifiable ground truth**.

AI hallucinations of statistics, release dates, version numbers, or project stars are strictly prohibited in publication-grade CofVid videos. All cited metrics must originate from `web_data_grounder` and be archived in `grounded_facts.json`.

---

## 1. When to Use Web Data Grounder

- **Research Stage**: Running an initial scan of a project, software repository, or product landing page to ground the script in reality.
- **Scene Planning & Scripting**: Extracting exact star counts, fork metrics, license classifications, primary programming languages, and maintainer details.
- **Graphic Cards**: Feeding exact numbers into `open_design_tool` (`stat_callout`, `split_screen`, `lower_third`).
- **Quality Gates**: Reviewer checks compare card copy against `grounded_facts.json` and reject fabricated claims.

---

## 2. Tool Contract & Arguments

```python
from tools.analysis.web_data_grounder import WebDataGrounderTool

grounder = WebDataGrounderTool()
result = grounder.execute({
    "url": "https://github.com/nexu-io/open-design",
    "entity_type": "auto",          # "auto" | "github" | "website" | "docs"
    "project_dir": "projects/my-video", # Optional: stores grounded_facts.json in project
    "output_path": "projects/my-video/grounded_facts.json" # Optional explicit path
})

facts = result.data["facts"]
# Access verified fields:
# facts["stars"], facts["forks"], facts["description"], facts["language"], facts["license"]
```

---

## 3. Extracted Data Schema

### GitHub Repositories (`entity_type="github"`)
When scanning a GitHub URL (`github.com/:owner/:repo`), the tool extracts:
- `name`: Repository name
- `full_name`: `owner/repo`
- `description`: Official repository bio / tagline
- `stars`: Stargazer count (`int`)
- `forks`: Fork count (`int`)
- `open_issues`: Active open issues / PR count (`int`)
- `language`: Dominant programming language (e.g., "TypeScript", "Python", "Rust")
- `topics`: Curated topic tags
- `license`: SPDX identifier or license name (e.g. "MIT", "Apache-2.0")
- `owner_avatar_url`: Maintainer avatar URL
- `created_at` / `updated_at`: ISO timestamp strings
- `html_url`: Canonical GitHub URL

### General Web Pages (`entity_type="website"`)
When scanning a standard website URL:
- `title`: Page `<title>` or `og:title`
- `description`: `og:description` or `<meta name="description">`
- `og_image`: Social share image URL
- `site_name`: `og:site_name` or domain name
- `canonical_url`: Canonical page URL
- `headings`: Top `h1` and `h2` section titles

---

## 4. Audit Trail Artifact: `grounded_facts.json`

Every invocation generates a persistent JSON artifact:
```json
{
  "source_url": "https://github.com/nexu-io/open-design",
  "entity_type": "github",
  "scanned_at": "2026-10-31T07:25:34.123456+00:00",
  "provenance": "github_api",
  "facts": {
    "name": "open-design",
    "full_name": "nexu-io/open-design",
    "stars": 1420,
    "forks": 128,
    "language": "TypeScript",
    "license": "MIT"
  }
}
```

The Reviewer skill reads this file during quality gate checks. Any discrepancy between on-screen text and `grounded_facts.json` triggers a `CRITICAL` finding.
