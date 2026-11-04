---
name: brand-icon
description: >
  Official authentic vector brand logos and UI icons for CofVid. Enforces zero AI
  hallucinations for corporate marks (GitHub, Docker, Python, React, Apple, AWS, etc.)
  and UI iconography. Resolves SVG snippets, SVG files, and PNG rasterizations.
metadata: { "tags": "brand, logo, icon, svg, ui, graphics, zero-hallucination" }
---

# Brand & Icon Resolver — Zero-Hallucination Vector Graphics

`brand_icon_tool` ensures that **no AI diffusion model (Imagen, Flux, Midjourney) is ever used to fabricate company logos or brand marks**. Generative diffusion models frequently misspell brand names, warp distinctive silhouettes, and hallucinate glyphs, degrading documentary credibility.

`brand_icon_tool` provides deterministic, high-resolution, vector-accurate SVGs from official vector catalogs, Simple Icons, and live website favicon fallbacks.

---

## 1. When to Use Brand Icon

- **Documentary & Explainer Cards**: Adding authentic brand marks (e.g. GitHub Octocat, Docker whale, Python dual snake, React atom) to `open_design_tool` title cards, lower thirds, and monumental stat callouts.
- **Data & Metric Displays**: Displaying repository stars, package downloads, or cloud architecture diagrams with official brand marks.
- **UI Elements**: Rendering clean 24x24 Lucide/Feather-style interface icons (`star`, `terminal`, `code`, `shield`, `database`, `check`, `alert-circle`).
- **Website Fallback**: Fetching genuine brand assets from a live URL when covering a new or niche product.

---

## 2. Tool Contract & Arguments

```python
from tools.graphics.brand_icon_tool import BrandIconTool

tool = BrandIconTool()
result = tool.execute({
    "brand_name": "github",          # Target brand slug or UI icon name
    "icon_type": "brand",            # "brand" | "ui"
    "variant": "default",            # "default" | "light" | "dark" | "monochrome"
    "output_format": "svg_snippet",  # "svg_snippet" | "svg_file" | "png_file"
    "site_url": "https://docker.com",# Optional site URL for favicon fallback
    "width": 64,                     # Dimension in px
    "height": 64,
})

svg_markup = result.data["svg"]
hex_color = result.data["hex_color"]
provenance = result.data["provenance"]
```

---

## 3. Supported Built-in Brands

Pre-baked, zero-network, pixel-perfect official vectors:
- **Developer & DevOps**: `github`, `docker`, `kubernetes`, `linux`, `rust`, `python`, `typescript`, `javascript`, `go`
- **Frontend & Frameworks**: `react`, `vue`, `tailwind`
- **Cloud & Platforms**: `aws`, `google`, `microsoft`, `apple`, `openai`, `anthropic`, `meta`
- **Data & Databases**: `postgres`, `redis`
- **Media & Social**: `youtube`, `twitter` (X), `discord`

*For any other brand not in the pre-baked list, the tool automatically resolves via Simple Icons CDN with local caching, or falls back to live website favicon extraction.*

---

## 4. UI Icons (`icon_type="ui"`)

Clean Lucide / Feather vector icons formatted with `stroke="currentColor"`, `fill="none"`, and `stroke-width="2"`:
- `star`: Stargazers, favorites, ratings
- `code`: Source code, syntax, logic
- `terminal`: CLI commands, shell execution
- `shield`: Security, verification, license
- `database`: Storage, SQL, persistence
- `check`: Success, completion
- `alert-circle`: Warnings, critical notices
- `globe`: Web, network, URLs
- `cpu`: Hardware, compute, processing
- `server`: Infrastructure, backend services
- `git-branch`: Version control, branches

---

## 5. Variants

- **`default`**: Official brand identity color (e.g., Python blue & yellow, Docker `#2496ED`, GitHub `#181717`).
- **`monochrome`**: Replaces fill and stroke with `currentColor`, making the SVG inherit the active typographic color in CSS.
- **`light`**: Forces fill/stroke to `#ffffff` for dark cards and terminal screens.
- **`dark`**: Forces fill/stroke to `#18181b` for high-contrast white paper themes.

---

## 6. Integration with Open Design

Any `open_design_tool` component accepts `brand_slug`, `brand_icon`, or `brand_name` in its `props`:

```python
from tools.graphics.open_design_tool import OpenDesignTool

open_design = OpenDesignTool()
card = open_design.execute({
    "component_type": "stat_callout",
    "theme_id": "dark-data",
    "props": {
        "brand_slug": "github",
        "kicker": "OPEN SOURCE ADOPTION",
        "stat": "42,800",
        "title": "GitHub Stargazers",
        "body": "Accelerating developer ecosystem adoption across 140 countries.",
        "meta": "VERIFIED VIA WEB_DATA_GROUNDER"
    }
})
```
