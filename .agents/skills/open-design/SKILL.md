---
name: open-design
description: >
  Anti-AI Slop editorial design system for CofVid. Use when authoring documentary,
  explainer, or motion-graphics cards, lower thirds, monumental stat callouts,
  split screens, timelines, or quote cards. Integrates 150+ Open Design design systems
  and tokens with HyperFrames and FFmpeg transparent overlays.
metadata: { "tags": "design, editorial, graphics, open-design, typography, anti-slop, hyperframes, transparent-video" }
---

# Open Design — Editorial & Motion Graphics for CofVid

Open Design brings **publication-grade graphic design, design tokens, and editorial typography** into CofVid. It is specifically designed to defeat **"AI Slop"** (generic purple/blue neon gradients, floating rounded pills, low-contrast text, meaningless 3D blobs) by grounding video graphics in real graphic design traditions: Swiss Modernism, Monocle / Financial Times editorial publishing, investigative journalism, and technical utilities.

---

## 1. When to Use Open Design

Activate `open_design_tool` during the **`assets`** and **`compose`** stages of:
- **`animated-explainer`**: Hero title cards, monumental statistics, timeline beats, and quote cards.
- **`documentary-montage`**: Archival lower-thirds, witness/speaker identification, chapter cards, split-screen comparisons, and transparent overlay titles.
- **`hybrid`**: Contextual data cards, code/data sidebars, and high-impact stat reveals over live footage.

---

## 2. Design System Theme Directory

Open Design includes **150+ curated design systems** located in `external/open-design/design-systems/`. You can specify any valid `theme_id`:

| Theme ID | Aesthetic Style | Best For | Reference |
| :--- | :--- | :--- | :--- |
| **`editorial`** / **`swiss-editorial`** | Warm paper surfaces, Georgia/Serif display type, ink darks, terracotta accent | History, economics, long-form documentary, investigative journalism | *Monocle, FT Weekend, NYT Magazine* |
| **`dark-data`** / **`trading-terminal`** | Deep slate/charcoal backgrounds, monospace metrics, cyan/sky accents | Finance, computing, AI, systems engineering, live telemetry | *Bloomberg, Datadog, TradingView* |
| **`minimalist-news`** / **`theverge`** | Crisp white/off-black, sharp geometric layout, high-contrast red accent | Breaking news, modern culture, tech scoops, investigative reports | *The Verge, Wired, Axios* |
| **`atelier-zero`** | Gallery parchment, editorial navy, refined serif display, strict borders | Architectural essays, art critiques, philosophy, literature | *Cereal Magazine, Kinfolk, Bauhaus* |
| **`bold`** | High-impact brutalist typography, massive scale, monochrome + vibrant punch | Provocative essays, hype sequences, counter-culture topics | *Nike, Off-White, Dazed* |
| **`linear-app`** / **`modern`** | Dark slate, subtle borders, crisp sans-serif, precision tech feel | Software architecture, developer tools, future technology | *Linear, Vercel, Raycast* |

---

## 3. Component Catalog & Props Specifications

Call `open_design_tool` with `mode: "template"` and one of the 6 canonical component types:

### A. Fullscreen Card (`fullscreen_card`)
Monumental title, chapter transition, or essay introduction.
```python
props = {
    "kicker": "ACT I // THE FOUNDATION",
    "title": "The Architecture of Tomorrow",
    "subtitle": "How decentralized protocols quietly replaced the industrial cloud.",
    "body": "Over twenty-four months, enterprise compute migrated away from centralized server farms into autonomous local runtimes.",
    "meta": "OCTOBER 2026 / COFVID RESEARCH ARCHIVE"
}
```

### B. Lower Third (`lower_third`)
Broadcast documentary identification for speakers, archival footage, or locations. Render with `output_format: "webm_alpha"` for direct overlay over B-roll.
```python
props = {
    "kicker": "WITNESS ARCHIVE",
    "name": "Dr. Elena Rostova",
    "role": "Lead Quantum Systems Architect, CERN",
    "meta": "GENEVA, SWITZERLAND • RECORDED 14:22 UTC"
}
```

### C. Stat Callout (`stat_callout`)
Monumental metric with editorial context. The number commands the canvas.
```python
props = {
    "kicker": "MEASURED OUTCOME",
    "stat": "84.2%",
    "title": "Reduction in Network Latency",
    "body": "Independent benchmarking across 1,400 distributed production clusters demonstrated near-zero packet loss during peak congestion.",
    "meta": "SOURCE: IEEE TRANSACTIONS ON DISTRIBUTED SYSTEMS (2026)"
}
```

### D. Split Screen (`split_screen`)
Side-by-side comparative analysis (Thesis vs. Antithesis, Legacy vs. Modern, Before vs. After).
```python
props = {
    "kicker": "COMPARATIVE AUDIT",
    "title": "Centralized Cloud vs. Autonomous Edge",
    "left": {
        "kicker": "CENTRALIZED",
        "title": "Legacy Cloud",
        "stat": "$140k/mo",
        "body": "Single point of failure with compounded recurring egress tolls."
    },
    "right": {
        "kicker": "DISTRIBUTED",
        "title": "Atelier Edge",
        "stat": "$1.2k/mo",
        "body": "Zero egress fees, deterministic local compilation, and zero-downtime execution."
    },
    "meta": "AUDIT PERIOD: Q1–Q3 2026"
}
```

### E. Timeline Step (`timeline_step`)
Chronological milestones, historical breakthroughs, or sequential phases.
```python
props = {
    "step_number": "03",
    "kicker": "CHRONOLOGY // PHASE III",
    "title": "The Microprocessor Revolution",
    "subtitle": "Silicon gate technology commoditizes computation.",
    "body": "The introduction of single-chip arithmetic logic units democratized computational horsepower, shifting it from military installations to personal desks.",
    "meta": "NOVEMBER 1971 • INTEL 4004"
}
```

### F. Quote Card (`quote_card`)
High-impact attributed citation with typographic authority.
```python
props = {
    "kicker": "PRIMARY TESTIMONY",
    "quote": "We shape our tools, and thereafter our tools shape us.",
    "author": "Father John Culkin (often attributed to Marshall McLuhan)",
    "role": "Director of the Center for Understanding Media",
    "meta": "SATURDAY REVIEW • MARCH 18, 1967"
}
```

---

## 4. Output Deliverables & Pipeline Integration

The tool supports three output formats via `output_format`:

1. **`dom_snippet` (Default)**:
   - Returns clean, standards-compliant HTML/CSS with injected CSS variables.
   - Ideal for **HyperFrames** HTML composition.
   - Paste directly into a HyperFrames scene `<div class="clip">...</div>` or save to `projects/<project-id>/assets/scenes/scene_03.html`.

2. **`png_still`**:
   - Renders a 1920×1080 (or custom aspect) crisp still image via headless Chrome.
   - Saves to `output_path` (e.g. `projects/<project-id>/assets/images/stat_card_01.png`).
   - Use in FFmpeg Pan-and-Scan (Ken Burns) or as slide overlays.

3. **`webm_alpha` (Transparent Video Overlay)**:
   - Compiles a transparent WebM video clip using Chrome headless + FFmpeg VP9 (`yuva420p` pixel format).
   - Can be overlaid seamlessly over B-roll, interview footage, or 3D animations:
     ```bash
     ffmpeg -i broll.mp4 -c:v libvpx-vp9 -i lower_third.webm -filter_complex "[0:v][1:v]overlay=0:0" final.mp4
     ```

---

## 5. Anti-AI Slop Principles

To maintain documentary and cinematic credibility, adhere to these rules:

1. **Restraint over Exuberance**: Never use more than ONE accent color per card. The typography, whitespace, and rules do the structural work.
2. **Real Typography Hierarchy**: Display headlines use authoritative Serifs (`Georgia`, `Charter`, `Iowan Old Style`) or stark Modern Grotesques. Metadata and kickers use Monospace (`IBM Plex Mono`, `JetBrains Mono`).
3. **No Decorative Blobs**: Avoid floating gradients, pastel pill tags, and cartoonish 3D glass balls. Use editorial lines, border dividers (`1px solid var(--border)`), and mono badges.
4. **Pacing**: In video timelines, hold stat cards and quote cards long enough to be read twice:
   $$\text{Duration} = \max\left(4.0, \frac{\text{word count}}{2.5}\right) \text{ seconds}$$
