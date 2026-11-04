# BÀN CỜ — Video Design System

> **COFFAT MEDIA · Channel Design Specification**  
> Version 2.1 · Format: vertical business / economics documentary · Aspect ratio: 9:16  
> **Master Visual System: Swiss Financial Bento Nguyên Khối (Integrated Monolith Architecture)**

## 1. Purpose and scope

BÀN CỜ explains business, economics, companies, markets, business models, industry competition, financial systems, and the strategic decisions that shape global organizations and economies.

This document is the visual source of truth for BÀN CỜ vertical video production: authentic industrial & corporate footage, executive typography, financial charts, balance sheet diagrams, subtitles, transitions, and reusable Hyperframe compositions.

**This is a video design system—not a website, app, financial dashboard, social banner, avatar, or thumbnail specification.**

### Design direction

- **Primary Style:** **Swiss Financial Bento Nguyên Khối** (Swiss Editorial Architecture × Bloomberg Originals Investigative Journalism × Apple Executive Keynote).
- **Mood:** analytical, composed, authoritative, credible, commercially literate, and architecturally structured.
- **Visual thesis:** demystify corporate strategies, market moats, unit economics, and capital allocation through disciplined, unified modular architecture—never through crypto hype or casino trading aesthetics.
- **Unified Monolith Architecture:** The entire 60-second runtime adheres to **ONE continuous visual universe**. Every scene shares the identical frosted glass bento card material, executive top HUD, typography hierarchy, and mathematical motion grammar.
- **Rule of White-Space Elimination (v2.1):** Zero dead whitespace policy. Large Bento compartments (>400px height) must NEVER leave cavernous white voids. Every card must either:
  1. Feature an **Inset Framed Media Window** (1px border, 10-12px radius, technical SEC/Bloomberg label tag, aspect ratio 16:9 or 21:9) showcasing authentic corporate/industrial footage or historical archival photos.
  2. Implement **Content-Aware Compact Scaling**: expand typography floor, thicken progress/waterfall bars (36-48px), and compact card padding so the frame feels dense, premium, and architecturally deliberate.

## 2. Core visual principles

1. **Bento Grid structural partitioning.** Partition complex corporate breakdowns into disciplined, asymmetric Bento-box modules (hero metric card, secondary ratio cards, operating breakdown, verified source footnote).
2. **Frosted glass card surfaces.** Containers feature crisp, modern frosted-card styling (`background: rgba(255, 255, 255, 0.90); backdrop-filter: blur(16px); border: 1px solid #E3E6E1; border-radius: 16px; box-shadow: 0 8px 24px rgba(25, 35, 30, 0.04);`) grounded on warm `paper` (`#FAFAF7`) with subtle coordinate grid lines.
3. **Data must be verifiable, dated, and sourced.** Every financial metric must state its exact accounting basis (e.g., `FY2025 GAAP`, `TTM`, `Q3 YoY`), currency symbol, and verified public filing source (`SEC 10-K`, `SEC Form 20-F`, `Annual Report`).
4. **Counter motion with mathematical restraint.** Financial metrics transition via smooth counter number rolls (`0 -> $42.5B`) that settle cleanly without slot-machine bounce.
5. **Separation of business reality from speculation.** Differentiate audited historical earnings from consensus analyst estimates or strategic forward projections.
6. **Real economy over abstract money worship.** Prioritize authentic footage of logistics hubs, container terminals, semiconductor cleanrooms, vehicle assembly lines, and corporate headquarters over stock money graphics.
7. **Disciplined accent encoding.** `forest-green` (`#376B50`) denotes primary growth, profitability, and highlighted mechanisms; `brass` (`#B18D55`) serves as historical benchmark or valuation cap.
8. **Executive Top HUD Monolith.** A permanent, slim frosted glass HUD at `y=140` anchors the narrative across all scenes, displaying the channel brand lockup, active security ticker, and audited filing basis.
9. **Inset Framed Media Integration.** High-resolution industrial photography and executive archive imagery are embedded directly inside Bento cards as Inset Windows, eliminating awkward empty gaps and anchoring the viewer's gaze.

## 3. Color system

### Base palette

| Token | Hex | Role |
|---|---|---|
| `paper` | `#FAFAF7` | Main warm-white graphic canvas; bento grid background |
| `white` | `#FFFFFF` | Frosted bento card fill; clean financial table surface |
| `ink` | `#242724` | Primary financial typography, numbers, and chart axes |
| `muted-ink` | `#70756F` | Secondary accounting labels, units, and footnote citations |
| `rule` | `#E3E6E1` | Bento card borders (`1px solid`) and financial gridlines |
| `deep` | `#19231E` | Contrast backing for executive keynote or dark corporate footage |

### Channel accents

| Token | Hex | Role |
|---|---|---|
| `forest-green` | `#376B50` | Primary accent; revenue growth, operating profit, market leader metric |
| `brass` | `#B18D55` | Secondary accent; valuation benchmark, historical baseline, debt ratio |
| `sage-gray` | `#E2E8E1` | Soft bento module grouping surface, muted comparison card backing |

### Color rules

- Bento compositions are anchored on `paper` (`#FAFAF7`) with `white` / frosted cards and `rule` (`#E3E6E1`) borders.
- Use `forest-green` (`#376B50`) for the primary metric card or dominant chart series.
- Use `brass` (`#B18D55`) strictly for benchmarks, industry averages, or debt/cost contrast.
- Never use toxic neon green or bright crimson trading colors; avoid binary red/green sensationalism.
- **Strict Anti-AI Palette Guardrail:** Strictly ban neon crypto greens, electric blues, flashing casino colors, black-and-gold luxury metallic gradients, or raining golden coin washes.

## 4. Typography

### Recommended families

| Purpose | Preferred | Alternatives |
|---|---|---|
| Main editorial headline | Source Serif 4 | Lora |
| Body and explanatory text | Inter | IBM Plex Sans / Manrope |
| Financial values, dates, units | IBM Plex Mono | Roboto Mono |
| Secondary labels | Inter | Manrope |

Serif headlines provide editorial authority; sans-serif keeps business explanations direct; mono supports precise financial figures and aligned values.

### Vertical-video type scale (1080 × 1920 reference)

| Role | Starting size | Weight | Guidance |
|---|---:|---:|---|
| Hero headline | 88–114 px | 600–750 | Concise claim or business question |
| Key statement | 62–82 px | 600–700 | Main finding or mechanism |
| Body explanation | 38–48 px | 400–500 | Short explanatory copy |
| Chart / diagram label | 28–36 px | 450–600 | Clear, short labels |
| Values / metadata | 22–30 px | 500–600 | Value, unit, period, source |
| Subtitles | 44–54 px | 500–600 | Maximum 2 lines |

### Typography rules

- Use sentence case for headlines unless a short label benefits from uppercase.
- Use tabular numerals or mono type for aligned values.
- Preserve currency symbols, decimal precision, negative signs, and units exactly.
- Keep display line-height around `0.98–1.1` and body line-height around `1.3–1.5`.
- Never shrink key financial values to fit a crowded chart; simplify the chart instead.
- Confirm full Vietnamese diacritics and international company names render correctly.

## 5. Canvas, composition, and Bento Grid layout

- **Master canvas:** `1080 × 1920 px`, portrait `9:16`.
- Keep essential text, bento metrics, chart axes, and company labels inside the safe area: Left/Right 90px, Top 140px, Bottom 300px.
- **Master Monolith Architecture:**
  - **Global Background Canvas:** Warm parchment `#FAFAF7` overlaid with a subtle 1px coordinate grid (`rgba(227, 230, 225, 0.45)`) and delicate faint chess coordinate watermark (`opacity: 0.03`).
  - **Standardized Bento Glass Material:**
    ```css
    background: rgba(255, 255, 255, 0.90);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid #E3E6E1;
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(25, 35, 30, 0.04);
    ```
    Every card in every scene adheres to this identical frosted material.
  - **Executive Top HUD Monolith (Continuous at `y=140`):**
    A slim frosted glass pill spanning `width: 900px`, `height: 52px`:
    - Left: Channel branding `BÀN CỜ` + `[SEC 20-F // GAAP AUDITED]` badge
    - Right: Real-time corporate ticker pill (e.g. `TSM $192.40 ▲+4.8%`) in `forest-green` & mono.
- **Asymmetric Bento Compartments:**
  - **Hero Metric / Focus Card (Upper 40–50%):** The primary strategic finding, dominant revenue chart, or core business model mechanism.
  - **Secondary Supporting Cards (Middle 25–35%):** Paired frosted cards displaying supporting KPIs (e.g., Left: `Operating Margin 42.1%`, Right: `Market Share 61.2%`).
  - **Source & Footnote Card (Bottom 8–12%):** Restrained, single-line verified filing citation (`Source: Form 20-F, SEC Filing FY2025 // audited`).
- Maintain strict mathematical alignment across column borders and baseline numbers.

## 6. Business imagery and footage direction

### Preferred material

- Authentic industrial, logistical, and retail environments: deepwater container ports, automated fulfillment centers, semiconductor cleanrooms, vehicle assembly lines, retail store floors.
- Genuine company products, verified packaging, documented consumer experiences, and official corporate headquarters.
- Real executive press conferences, shareholder presentations, and verified regulatory hearing recordings.
- Original corporate annual reports, SEC filing tables (Form 10-K, 10-Q, 20-F), earnings call slides, and Bloomberg terminal data charts.

### Image treatment

- Natural, documentary color grading; avoid glossy luxury advertising filters or artificial contrast.
- Focus on real physical operations and unit-level economics rather than abstract financial symbols.
- Precise 1px callout lines and tabular data insets linking footage to financial cards.
- Embedded video windows inside frosted bento frames with subtle 1px border.
- Preserve document legibility: crop to the exact table row or balance sheet item being discussed.

### Strict Anti-AI Guardrails (Do Not Use)

- **Flashing red/green crypto candlestick charts:** Strictly ban frantic stock-ticker animations, green neon bull market arrows, or red flashing crash alerts.
- **Raining gold coins & cash stacks:** Absolutely ban flying dollar bills, heaps of banknotes, 3D piggy banks, or spinning gold coins.
- **Generic AI businessmen:** Never use Midjourney-generated men in generic blue suits shaking hands in glass skyscrapers.
- **Fake trading dashboards:** Fabricated Bloomberg terminals, simulated Robinhood portfolio gains, or invented market tickers.
- **Luxury lifestyle flexes:** Supercars, private jets, or champagne toasts used as visual stand-ins for business competence.

## 7. Bento Grid financial visualization & corporate metrics

Data is the foundation of BÀN CỜ. Every financial metric must be designed with annual-report rigor.

- **Bento Metric Counter:** Large hero figures rendered in `IBM Plex Mono` / `Inter` (`72–96px`, weight `700`) with precise currency and denomination tags (`$142.8B`).
- **Verified Source Footnotes:** Every card displays tiny, unmissable provenance at its lower edge (e.g., `SEC 10-K Q4 2025 | GAAP Operating Income`).
- **Unit Economics Breakdown:** Use bento sub-cards to show the equation: `Revenue ($100)` − `COGS ($35)` − `OpEx ($40)` = `Operating Margin ($25)`.
- **Financial Chart Rules:**
  - **Trend over time:** Clean line series in `forest-green` (`#376B50`) with muted gray comparison baseline.
  - **Competitive share:** Horizontal bar chart comparing rivals, highlighted with `forest-green` for the protagonist firm and neutral gray for competitors.
  - **Valuation benchmarks:** Brass (`#B18D55`) used exclusively for industry multiples (P/E, EV/EBITDA, Price/Sales).

## 8. Motion and transitions

Motion in Swiss Financial Bento embodies the precision, composure, and elegance of an Apple keynote combined with a Bloomberg documentary.

### Preferred motion

- **Bento Card Stagger Entrance:** Bento cards animate in with subtle stagger (`stagger: 0.08s`), scaling smoothly from `0.98 -> 1.0` with soft opacity fade (`power3.out`).
- **Financial Counter Transitions:** Numbers count up smoothly from zero to their audited values (`0 -> $84.2B`) over 0.8s–1.2s using an exponential ease (`power2.out`).
- **Progressive Bar / Line Trace:** Financial charts draw from left to right or grow from baseline in sync with the narrator's vocal disclosure.
- **Focus Shift Motion Grammar:** As narration progresses through different business components, non-active bento cards softly dim (`opacity: 0.42`), while the active focus card scales subtly to `1.02` with crisp border highlight (`#376B50` or `#242724`).
- **Clean Jump Cuts:** Crisp transitions between authentic operational footage and financial bento analysis boards, always tied together by the continuous Top HUD and coordinate grid canvas.

### Motion constraints

- Strictly avoid casino-like spinning slot reels, rapid ticker scrolls, or erratic bounce.
- Strictly avoid flashing red/green pulses that mimic speculative trading apps.
- Motion must respect fiduciary gravity; never sacrifice readability for kinetic spectacle.
- Final frame must remain 100% legible, balanced, and screenshot-ready.

## 9. Subtitle and on-screen text system

- Use concise spoken sentences, maximum two lines.
- Default to dark `ink` text on a warm-white frosted plate (`background: rgba(250, 250, 247, 0.9); border: 1px solid #E3E6E1`).
- Highlight one critical financial metric, growth figure, or business term in `forest-green` (`#376B50`).
- Use `brass` (`#B18D55`) strictly for secondary benchmark figures; never color whole sentences.
- Never let subtitles collide with bento cards, financial charts, or source footnotes.
- Maintain consistent placement in the lower safe area.

## 10. Reusable scene patterns

1. **Business hook:** a clear business question, counterintuitive finding, or documented claim.
2. **Real-world context:** show the company, product, industry, market, or operation.
3. **Bento mechanism:** partition the company's business model or unit economics into frosted bento cards.
4. **Evidence & Chart:** a sourced financial chart or annual-report balance sheet excerpt with verified footnotes.
5. **Trade-off / Moat:** show the competitive threat, regulatory hurdle, or capital expenditure barrier.
6. **Strategic implication:** end with what the mechanism means for the company, market, customer, or economy.

## 11. Financial and business integrity

- Never invent revenue, profit, valuation, market share, customer count, growth rate, or financial projections.
- Show the date and period for time-sensitive numbers; distinguish quarterly, annual, trailing-twelve-month, and point-in-time values.
- Preserve currency and units. Do not compare nominal values across currencies or periods without explaining the basis.
- Distinguish reported figures, estimates, forecasts, and editorial calculations.
- Do not imply investment advice or guaranteed returns through the visual language.
- Keep chart scales honest and show relevant caveats when a comparison is not like-for-like.
- Identify the source of key financial claims in production notes and on-screen where useful.

## 12. Anti-patterns

- **Crypto / Casino visual tropes:** Flashing red/green candlesticks, rocket ship icons, flying dollar bills, neon trading tickers.
- **Generic AI business clichés:** Midjourney-generated businessmen in suits, fake handshake photos, generic glass skyscrapers with sun flares.
- **Fabricated numbers:** Fake financial dashboards, unlabelled chart axes, or unattributed percentage claims.
- **Gold foil luxury aesthetics:** Black-and-gold metallic gradients, 3D shiny coins, or private jet lifestyle montages.
- **Chart clutter:** Cramming multiple competing charts into one vertical frame without modular bento separation.
- **Missing source citations:** Presenting financial metrics without stating accounting period (FY, Q, TTM) or source filing.

## 13. Hyperframe implementation guidance

- Create reusable **Bento grid financial compositions**: executive bento hero, unit-economics breakdown board, competitive market-share comparison, financial statement balance sheet card, and closing strategic takeaway.
- Structure layouts with modular CSS Grid / Flexbox bento cards, frosted backdrop filters, and 1px borders (`#E3E6E1`).
- Tokenize `paper` (`#FAFAF7`), `white` (`#FFFFFF`), `ink` (`#242724`), `forest-green` (`#376B50`), `brass` (`#B18D55`), `sage-gray` (`#E2E8E1`), and `rule` (`#E3E6E1`).
- Calibrate GSAP counter animations for tabular numbers (`IBM Plex Mono`) with comma-separated formatting.
- Support full-bleed industrial/operational footage with minimal floating frosted data chips.
- Never bake financial numbers, source citations, or subtitles into background images.

## 14. Quality checklist

- [ ] Output is vertical `1080 × 1920` (`9:16`).
- [ ] Essential text, bento cards, numbers, and footnotes respect safe areas (Left/Right 90px, Top 140px, Bottom 300px).
- [ ] Graphic frames adhere to **Style 3 — Bento Grid Financial Motion** with frosted cards and verified source footnotes.
- [ ] Financial metrics state exact accounting period (e.g., FY2025, Q3 YoY, TTM) and currency.
- [ ] Palette accents are disciplined: `forest-green` (`#376B50`) for core growth/margins; `brass` (`#B18D55`) for benchmarks.
- [ ] Operational footage showcases real factories, logistics, stores, or executive events.
- [ ] Motion is smooth and executive-grade (staggered bento card entrance, smooth number counters, zero slot-machine bounce).
- [ ] Subtitles do not obscure bento cards, chart axes, or source citations.
- [ ] **Strict Anti-AI Verification:** Absolutely zero flashing red/green crypto candlesticks, raining gold coins, or generic AI businessmen in suits.
