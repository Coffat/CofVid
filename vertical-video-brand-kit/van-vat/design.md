# VẠN VẬT — Video Design System

> **COFFAT MEDIA · Channel Design Specification**  
> Version 2.0 · Format: vertical science / nature documentary · Aspect ratio: 9:16  
> **Official Approved Style: National Geographic Field Journal & Museum Specimen (2026 Standard)**  
> **Motion Standard: Full 5-Pillar Master Scientific Motion Suite (Focus Racking + Caliper + Da Vinci + Fibonacci + Wax Seal)**

## 1. Purpose and scope

VẠN VẬT explores science, the universe, physics, biology, Earth systems, animals, plants, and the natural world. Its job is to make complex phenomena understandable while preserving their scale, beauty, and scientific integrity.

This document is the visual source of truth for VẠN VẬT storyboards, video scenes, diagrams, subtitles, transitions, and reusable Hyperframe compositions.

**This is not a website, app, dashboard, social banner, avatar, or thumbnail specification.** It governs vertical video frames only.

### Design direction

- **Primary Style:** **National Geographic Field Journal & Museum Specimen** (Sổ tay Thám hiểm Dã ngoại & Tiêu bản Bảo tàng Hàn lâm) × Minimalist Blueprint / Scientific Diagram.
- **Mood:** curious, contemplative, architecturally precise, tactile, disciplined, quietly wondrous, academic authority.
- **Visual thesis:** The natural and physical world is already extraordinary in its mathematical precision; design should reveal its hidden blueprints and structures, not replace it with AI fantasy.
- **Primary principle:** Warm parchment field journal canvas (`#FAF6EE` / `#FAFAF7`), double-ruled museum specimen framing, high-precision Vernier caliper dimensioning, Leonardo da Vinci calligraphic anatomical leader lines, living Fibonacci overlays, and authentic museum wax seal provenance stamps.

The result should feel like an elite expedition journal or Smithsonian / Royal Society monograph. It strictly eliminates fantasy AI biology renders, oversaturated neon animal morphs, and ungrounded sci-fi space artwork.

## 2. Core visual principles

1. **Let the real subject lead with authentic footage.** Show the real organism, geological strata, biological specimen, celestial body, or physics experiment directly without synthetic filters.
2. **Minimalist Blueprint / Scientific Diagram as the explanatory medium.** Anatomical structures, orbital paths, and physical mechanics are rendered as razor-sharp architectural linework, technical hatching, and cross-sections.
3. **Micro/macro scale bars on every dimensional reveal.** Every magnification or astronomical zoom must feature an explicit, authenticated scale bar (e.g., `100 µm`, `5 mm`, `1 AU`, `10 light-years`) with unit annotations.
4. **Fine trajectory and vector mechanics.** Celestial orbits, electromagnetic fields, photon paths, and fluid vectors are delineated with fine architectural drafting lines (`0.75px–1.5px`) and coordinate guides.
5. **Use warm white and paper tones as graphic canvas.** Explanatory diagrams, blueprint cross-sections, and comparison charts sit on `paper` (`#FAFAF7`); authentic space, ocean depths, and night-sky footage remain full-screen.
6. **Precision palette with natural fidelity.** Accents `botanical-teal` (`#397B72`), `mineral-blue` (`#83A7B4`), and `sand` (`#E3D8BE`) highlight anatomical layers and vector paths while wildlife and astronomical footage retains 100% true-to-life coloration.
7. **Give every diagram room to breathe.** Maintain generous negative space; never clutter a frame with decorative scientific formulas or ungrounded symbols.

## 3. Color system

### Base palette

| Token | Hex | Role |
|---|---|---|
| `sand-light` | `#FAF6EE` | Primary warm field-journal parchment background; specimen mount plate |
| `paper` | `#FAFAF7` | Clean warm-white scientific paper; technical diagram canvas |
| `white` | `#FFFFFF` | Editorial contrast plates and specimen card containers |
| `ink` | `#242624` | Primary body text, scientific typography, and fine drafting linework |
| `muted-ink` | `#70736E` | Secondary annotations, scale ticks, and taxonomical catalog labels |
| `rule` | `#E6E5DF` | Double-ruled museum borders, coordinate gridlines, and guides |
| `deep` | `#172321` | Occasional dark natural-science, deep-ocean, or cosmic contrast canvas |

### Channel accents

| Token | Hex | Role |
|---|---|---|
| `antique-gold` | `#B18B55` | Vernier calipers, Fibonacci spirals, museum wax seal stamps |
| `botanical-teal` | `#397B72` | Primary accent for biological structures, life systems, and cellular boundaries |
| `mineral-blue` | `#83A7B4` | Secondary accent for aquatic, atmospheric, cryospheric, and celestial trajectories |
| `sand` | `#E3D8BE` | Earth/mineral tone for geological formations, fossil mounts, and museum specimen tags |

### Color rules

- Explanatory diagram frames are anchored on `paper` (`#FAFAF7`) with precision `ink` (`#242624`) architectural linework.
- Use `botanical-teal` (`#397B72`) for the primary highlighted organ, biological pathway, or focal mechanism.
- Use `mineral-blue` (`#83A7B4`) for trajectories, fluids, atmospheric layers, and orbital paths.
- Use `sand` (`#E3D8BE`) for comparative scale references and geological stratification.
- **Strict Anti-AI Guardrail:** Never apply radioactive greens, neon magenta animal highlights, glowing aura outlines, or sci-fi space nebula gradients. Preserve true natural coloration in wildlife and documentary footage.

## 4. Typography

### Recommended families

| Purpose | Preferred | Alternatives |
|---|---|---|
| Main editorial headline | Source Serif 4 | Lora |
| Large explanatory sans | Inter | Manrope |
| Body and captions | Inter | IBM Plex Sans |
| Scientific labels, values, units | IBM Plex Mono | Roboto Mono |

Serif typography gives the channel a measured editorial character; sans-serif typography keeps science explanations clear. Use mono sparingly for measurements, taxonomy, dates, and units.

### Vertical-video type scale (1080 × 1920 reference)

| Role | Starting size | Weight | Guidance |
|---|---:|---:|---|
| Hero headline | 88–112 px | 600–700 | Editorial, short, 2–4 lines |
| Section / key statement | 62–80 px | 600–700 | A question, discovery, or core concept |
| Body explanation | 38–48 px | 400–500 | Short, digestible lines |
| Figure / diagram label | 28–36 px | 450–600 | Clear scientific naming |
| Measurement / metadata | 22–28 px | 500–600 | Unit, scale, classification, source |
| Subtitles | 44–54 px | 500–600 | Maximum 2 lines |

Tune sizes for the amount of text and the actual image. Do not compress a long scientific explanation into one frame; divide it into sequential scenes.

### Typography rules

- Use serif headlines for curiosity and editorial emphasis, not for dense labels.
- Use sans-serif for explanation and labels.
- Use mono for values and units only where it improves scanning.
- Keep line-height around `0.98–1.12` for display and `1.3–1.5` for explanatory copy.
- Ensure all typefaces support Vietnamese diacritics and scientific symbols used in the script.

## 5. Canvas, composition, and safe area

- **Master canvas:** `1080 × 1920 px`, portrait `9:16`.
- Keep essential text, labels, scales, and diagram annotations approximately 90 px from left/right, 140 px from top, and 300 px from bottom.
- Validate the exact bottom safe zone against the target platform before publishing.
- Use large visual subjects and clean negative space; small scientific details need a deliberate close-up or an inset.
- Prefer asymmetrical editorial compositions: image or illustration on one side, concise text on the other.
- Use a center composition for a single specimen or astronomical object only when it creates a clear focal point.
- Maintain consistent alignment for figure labels, captions, scale bars, and section headings.

## 6. Image, footage, and illustration direction

### Preferred material

- Real wildlife, marine species, botanical specimens, geological formations, weather dynamics, and real electron/optical microscopic footage.
- Verified astrophysical observations and scientifically calibrated imagery from credible space agencies (NASA, ESA, James Webb, Hubble, ESO).
- High-resolution scientific specimen photography, museum collection scans, and authentic laboratory research documentation.
- Minimalist architectural blueprint illustrations: anatomical cross-sections, cutaways, isometric physics models, and orbital mechanics diagrams.

### Image treatment

- Preserve realistic organic textures, earthy tones, and true biological coloration. Absolutely no hyper-saturated fantasy color grades.
- Always include an explicit scale bar and unit marker when conveying dimensions (from microscopic nanometers to cosmic astronomical units).
- Use fine architectural callout lines (`0.75px–1.5px`), circular reticles, and crisp `IBM Plex Mono` labels for anatomical or physical parts.
- Clearly differentiate direct optical/telescope footage from artist-rendered scientific reconstructions or blueprint models.

### Strict Anti-AI Guardrails (Do Not Use)

- **Fantasy AI biology renders:** Grotesque hybrid creatures, imaginary speculative organisms presented without disclaimer, or synthetic plastic-skinned animals.
- **Oversaturated neon animal morphs:** Fluorescent glowing fur, bioluminescent psychedelic plants where none exist, or neon animal eyes.
- **Ungrounded sci-fi space artwork:** Swirling purple-cyan fantasy nebulas, invented exploding planets, fake black holes with glowing halos, or fictional starships.
- **Decorative 3D clichés:** Floating glowing DNA double helices without genetic context, generic rotating Bohr-model atoms, or detached translucent 3D brains.
- **Fabricated anatomy:** Generative illustrations containing erroneous bone counts, impossible limb joints, or fictitious organ topologies.

## 7. National Geographic Field Journal & Museum Specimen Language

VẠN VẬT chuẩn hóa ngôn ngữ thị giác theo phong cách **Sổ tay Thám hiểm Dã ngoại & Tiêu bản Bảo tàng**:

- **Khung Tiêu Bản Viền Chỉ Đôi (Double-Ruled Specimen Plate):** Các mẫu vật sinh học, khoáng thạch, hóa thạch hoặc hiện tượng tự nhiên được đặt trang trọng trong khung chỉ đôi thanh lịch (`#DED8CF` / `#C7B58E`) trên nền giấy da ngả vàng dã ngoại `sand-light` (`#FAF6EE`).
- **Danh Pháp Quốc Tế La-Tinh (Binomial Nomenclature):** Mọi sinh vật đều có nhãn danh pháp khoa học in nghiêng trang trọng bằng font `Source Serif 4` (ví dụ: *Nautilus pompilius*, *Apis mellifera*), đi kèm phân loại ngành học (`PHYLUM`, `CLASS`, `FAMILY`).
- **Thước Kẹp Trắc Địa Đồng Thau (Antique Brass Vernier Caliper):** Thước kẹp đo đạc cơ học với vạch khắc milimet sắc sảo, ôm sát hai mỏ kẹp vào mẫu vật để hiển thị kích thước thực nghiệm.
- **Vạch Giải Phẫu Da Vinci (Da Vinci Leader Lines):** Các đường nét mực uốn lượn mềm mại kết nối từ các cơ quan nội tại ra các card chú giải giải phẫu.
- **Lớp Phủ Hình Học Thiêng (Sacred Geometry & Fibonacci Overlay):** Đường xoắn ốc vàng $\varphi = 1.618$ hoặc mạng lưới đối xứng lục giác $120^\circ$ phủ nhẹ lên mẫu vật để chứng minh quy luật toán học tuyệt mỹ của tự nhiên.
- **Triện Sáp Xác Thực Bảo Tàng (Museum Wax Seal):** Con dấu sáp nổi màu vàng antique gold (`#B18B55`) hoặc đỏ sậm (`#8B1E1E`) xác nhận tính nguyên bản và độ tin cậy khoa học của tiêu bản (`NATURAL HISTORY ARCHIVES · VERIFIED PRIMARY SOURCE`).

---

## 8. Motion and transitions (Bộ 5 Trụ Cột Chuyển Động Chuyên Nghiệp 2026)

Chuyển động trong VẠN VẬT tuân thủ nghiêm ngặt **Full 5-Pillar Master Scientific Motion Suite**:

### 1. Microscope Focus Racking (Lấy Nét Kính Hiển Vi Mở Đầu)
- Khi bắt đầu cảnh, mẫu vật chuyển từ mờ quang học sang sắc nét (`filter: blur(8px) -> blur(0px)`, `scale: 1.08 -> 1.0`, thời gian 1.0s - 1.2s, `ease: "power2.out"`).
- Đồng bộ cùng thước ngắm reticle quang học (`Plan-APO 4x / 0.16`), tái hiện cảm giác nhà khoa học đang xoay núm vi chỉnh tiêu cự để "khóa nét" đối tượng.

### 2. Precision Caliper Dimensioning (Thước Kẹp Đo Mẫu Vật Nhảy Số)
- Thước kẹp đồng trượt vào từ góc màn hình, hai mỏ kẹp áp sát hai cực mẫu vật.
- Đồng thời, số đo kích thước nhảy counter liên tục từ 0 lên số đo thực tế chính xác (ví dụ: `184.2 mm (±0.05)` hoặc `72.4 µm`) trong 0.8s - 1.2s.

### 3. Da Vinci Calligraphic Leader Lines (Đường Giải Phẫu Nét Mực)
- Các đường chỉ dẫn giải phẫu vẽ uốn cong mềm mại theo dáng dấp bản thảo Leonardo da Vinci (`DrawSVG`, nét mảnh `1px`, màu `ink` `#242624` hoặc `botanical-teal` `#397B72`), kết nối mượt mà từ nội quan ra nhãn định danh La-tinh.

### 4. Living Fibonacci & Geometric Overlay (Đường Xoắn Ốc Vàng Tự Nhiên)
- Đường cong xoắn ốc vàng $\varphi = 1.618$ óng ánh vẽ tỏa ra từ tâm mẫu vật (`strokeDashoffset: 1000 -> 0`, thời gian 1.5s - 2.0s), ôm trọn cấu trúc buồng khí hoặc cánh hoa.

### 5. Museum Wax Seal Slam (Con Dấu Sáp Bảo Tàng Dập Nổi)
- Triện sáp nổi viện bảo tàng rơi dập dứt khoát xuống góc dưới (`scale: 1.35 -> 1.0`, `rotation: -4deg`, `ease: "back.out(2.2)"`), đóng dấu chứng nhận tiêu bản nghiên cứu.

### Motion constraints
- Nghiêm cấm hoàn toàn các hiệu ứng nổ hạt particle game 3D, vệt phát sáng laser sci-fi, hoặc xoay 3D lòe loẹt.
- Giữ vững nhịp điệu tĩnh tại, hàn lâm, uy tín và chuẩn mực của viện nghiên cứu tự nhiên hàng đầu.

## 9. Subtitle and on-screen text system

- Use short sentence-level subtitles, no more than two lines.
- Default to dark `ink` text on a warm-white plate over visually busy footage.
- On dark cosmic or deep-ocean footage, use white text on a restrained dark plate (`#172321`).
- Highlight scientific names, taxonomic terms, or core discoveries using `botanical-teal` (`#397B72`); use `mineral-blue` (`#83A7B4`) for secondary physical units or trajectories.
- Keep taxonomy, units, dates, and source notes distinct from subtitles.
- Never place subtitles over a specimen feature, animal face, graph scale, or critical annotation.
- Keep subtitle placement consistent within the safe area.

## 10. Reusable scene patterns

1. **Scale reveal:** introduce the subject, then reveal its size relative to a familiar reference.
2. **Specimen / phenomenon:** give a real image room to dominate, with a restrained editorial title.
3. **Inside the subject:** use a cross-section or cutaway to explain internal structure.
4. **How it happens:** present a sequential process diagram, one step at a time.
5. **Evidence / observation:** show a real image, measurement, source, experiment, or observation with concise attribution.
6. **Wonder / implication:** end with one meaningful consequence, unanswered question, or change of perspective.

Treat these as scene patterns, not a compulsory sequence. Use only those that help the particular topic.

## 11. Scientific integrity and source handling

- Never fabricate a scientific image, measurement, experiment, quotation, or finding.
- Do not present a conceptual illustration as a photograph or direct observation.
- Distinguish accepted evidence, active research, hypothesis, and speculation in the script and visual labels.
- Preserve units and scale. Do not remove a qualifier that changes the meaning of a number.
- If footage is illustrative rather than directly related to the exact species or phenomenon, avoid captions that imply it is documentary evidence of that specific subject.
- Keep source attribution readable but visually subordinate.

## 12. Anti-patterns

- **Fantasy AI biology & creatures:** AI-generated animals with mutant features, plastic skin, impossible limb counts, or fabricated speculative species presented without context.
- **Oversaturated neon nature:** Bioluminescent fluorescent glows applied to ordinary organisms, neon green moss, electric purple space vistas.
- **Sci-fi space clichés:** Spinning 3D wormholes, uncalibrated psychedelic nebulas, fictional laser-beam phenomena, and fake cosmic explosions.
- **Decorative 3D molecular filler:** Floating rotating DNA models, generic atoms with orbiting electron rings used as lazy scientific wallpaper.
- **Unverified anatomical cuts:** Drawing internal organs or biological pathways without verified anatomical reference.
- **Overcrowded infographics:** Cramming multiple competing diagrams or unreadable microscopic labels into a single portrait scene.

## 13. Hyperframe implementation guidance

- Create reusable **minimalist blueprint compositions**: specimen blueprint hero, anatomical cross-section cutaway, micro/macro scale zoom comparison, orbital trajectory map, laboratory process sequence, and closing takeaway.
- Keep titles, anatomical labels, scale bars, unit indicators, and subtitles as independent, editable layers.
- Tokenize `paper` (`#FAFAF7`), `ink` (`#242624`), `botanical-teal` (`#397B72`), `mineral-blue` (`#83A7B4`), `sand` (`#E3D8BE`), and blueprint linework rules (`#E6E5DF`).
- Calibrate DrawSVG stroke animations for blueprint vectors (`0.75px–1.5px`) with clean start/end points.
- Support authentic full-bleed footage with delicate 1px HUD scale overlays.
- Never bake labels, scale bars, or subtitles into background images.

## 14. Quality checklist

- [ ] Output is vertical `1080 × 1920` (`9:16`).
- [ ] Essential text, labels, and scale bars respect safe areas (Left/Right 90px, Top 140px, Bottom 300px).
- [ ] Graphic frames follow **National Geographic Field Journal & Museum Specimen** trên nền giấy da ngả vàng dã ngoại `sand-light` (`#FAF6EE`) và viền chỉ đôi bảo tàng.
- [ ] **Full 5-Pillar Motion Standards**:
  - [ ] Microscope Focus Racking: Lấy nét quang học `blur(8px) -> 0px` khi bắt đầu cảnh.
  - [ ] Vernier Caliper: Thước kẹp đồng trượt đo mẫu vật nhảy số counter chính xác.
  - [ ] Da Vinci Leader Lines: Đường chỉ dẫn giải phẫu vẽ nét mực cong mềm mại tới nhãn danh pháp La-tinh in nghiêng.
  - [ ] Fibonacci Overlay: Đường xoắn ốc vàng $\varphi = 1.618$ vẽ tỏa ra từ tâm ôm trọn cấu trúc mẫu vật.
  - [ ] Museum Wax Seal: Triện sáp nổi viện bảo tàng màu antique gold dập dứt khoát xác thực tiêu bản.
- [ ] Natural footage preserves authentic biological, geological, and astronomical colors.
- [ ] Palette accents are disciplined: `antique-gold` (`#B18B55`), `botanical-teal` (`#397B72`), `mineral-blue` (`#83A7B4`), `sand` (`#E3D8BE`).
- [ ] Motion is steady and scientific (DrawSVG blueprint linework, smooth calibrated zooms, zero video-game particles).
- [ ] Subtitles do not obscure specimens, cross-sections, or scale bars.
- [ ] **Strict Anti-AI Verification:** Absolutely zero fantasy AI biology renders, oversaturated neon animal morphs, or ungrounded sci-fi space artwork.
