# DẤU MỐC — Video Design System

> **COFFAT MEDIA · Channel Design Specification**  
> Version 2.0 · Format: vertical history documentary · Aspect ratio: 9:16  
> **Official Approved Style: Style 6 — Vox Paper Collage & Archival Documentary**  
> **Motion Standard: Continuous 2.5D Camera Drift & Full 5-Evidence Props Toolkit (Vox Approved)**

## 1. Purpose and scope

DẤU MỐC tells stories about history, civilizations, inventions, historical figures, conflicts, discoveries, and turning points that changed the world.

This document defines the channel's visual language for vertical videos: title frames, historical imagery, maps, timelines, document details, captions, motion, and reusable Hyperframe compositions.

**It is not a website, app, dashboard, banner, avatar, or thumbnail design specification.**

### Design direction

- **Primary Style:** **Style 6 — Vox Paper Collage & Archival Documentary** (Historical Document & Newspaper Cutout) × Historical Editorial × Contemporary Documentary.
- **Mood:** thoughtful, authoritative, human, atmospheric, tangible, and evidence-conscious.
- **Visual thesis:** history should feel like a documented investigation through tangible primary evidence—not a Hollywood costume-drama filter or plastic AI reenactment.
- **Primary principle:** authentic archival newspaper clippings, scanned historic B&W photos with torn-paper cutouts, original battle/voyage maps with animated pencil/route lines, punctuated by burgundy ink highlighter (`#873F43`) and antique-gold wax seal accents (`#B18B55`).

The channel should feel like a premier Vox-style historical investigative documentary. Every scene grounds the viewer in genuine historical artifacts, strictly eliminating AI-generated fantasy figures or synthetic plastic faces.

## 2. Core visual principles

1. **Evidence is the visual foundation.** Ground every story in authentic archival photographs, original documents, historical newspaper clippings, maps, letters, treaties, and museum artifacts.
2. **Vox-Style Paper Collage composition.** Layer authentic primary sources using crisp paper cutout aesthetics, subtle paper drop-shadows (`rgba(0,0,0,0.12)`), tactile torn-paper edges on historical clippings, and warm parchment surfaces (`#E8DFD0` / `#FAF8F3`).
3. **Animated pencil & route lines on original maps.** Track military campaigns, maritime voyages, and trade routes by animating hand-drawn pencil/ink paths directly over original cartographic scans.
4. **Burgundy ink highlighter & wax seal accents.** Emphasize critical turning points, treaty signatures, or explosive headlines with translucent burgundy highlighter strokes (`rgba(135, 63, 67, 0.25)`) and wax seal / stamp accents (`#B18B55`).
5. **Show chronology with uncompromising clarity.** Dates, geopolitical sequences, and cause-and-effect relationships must be immediate and clear.
6. **Strictly authentic human faces over generative fakes.** Never substitute a real historical person or soldier with an AI-generated portrait. When primary photography is unavailable, use verified museum engravings, statues, or explicitly stamped illustrative diagrams.
7. **Transparent reconstruction labeling.** Any necessary illustrative diagram or modern re-enactment must bear the mandatory stamp: `[TÁI HIỆN MINH HỌA // AI RECONSTRUCTION]`.

## 3. Color system

### Base palette

| Token | Hex | Role |
|---|---|---|
| `paper` | `#FAF8F3` | Main warm archival-paper background; tactile document surface |
| `parchment` | `#E8DFD0` | Historical paper clippings, antique document cutout backing |
| `white` | `#FFFFFF` | Clean editorial contrast plates and newspaper masthead cards |
| `ink` | `#292624` | Primary body text, newspaper typography, and archival linework |
| `muted-ink` | `#716B63` | Secondary citations, dates, archive provenance notes |
| `rule` | `#DED8CF` | Fine paper borders, timeline guides, and map coordinates |
| `deep` | `#211D1B` | Contrast shadow backing, dark photographic vignette frames |

### Channel accents

| Token | Hex | Role |
|---|---|---|
| `burgundy` | `#873F43` | Primary accent; key turning-point dates, chapter headers, ink highlighter wash |
| `antique-gold` | `#B18B55` | Secondary accent; wax seal badges, medal/artifact callouts, compass roses |
| `sepia-tint` | `#D4C4B5` | Archival photographic mount or secondary document clipping tone |

### Color rules

- Use `paper` (`#FAF8F3`) and `parchment` (`#E8DFD0`) as the dominant graphic canvas for collage layouts.
- Use `burgundy` (`#873F43`) for the central turning-point date, decisive battle, or critical treaty clause.
- Use `antique-gold` (`#B18B55`) for archival seals, map scales, and museum artifact callouts—never as gaudy metallic foil.
- Preserve authentic monochrome/patina in historical photographs and artifacts; do not artificially colorize historic photos unless verified.
- **Strict Anti-AI Palette Guardrail:** Absolutely ban universal sepia mud-washes, dramatic cinematic red/black vignette gradients, or garish digital high-contrast grading.

## 4. Typography

### Recommended families

| Purpose | Preferred | Alternatives |
|---|---|---|
| Main editorial headline | Source Serif 4 | Cormorant Garamond |
| Supporting text and subtitles | Inter | IBM Plex Sans / Manrope |
| Dates, coordinates, catalog labels | IBM Plex Mono | Roboto Mono |

Serif headlines establish historical character; a modern sans-serif keeps explanations readable. Use mono for date strings, coordinates, catalog references, and archive labels—not for long prose.

### Vertical-video type scale (1080 × 1920 reference)

| Role | Starting size | Weight | Guidance |
|---|---:|---:|---|
| Hero headline | 88–114 px | 600–700 | Strong editorial line breaks, 2–4 lines |
| Chapter / event title | 64–82 px | 600–700 | Name the person, event, or turning point |
| Narrative support | 38–48 px | 400–500 | Short phrases, readable on mobile |
| Document / map label | 28–36 px | 450–600 | Concise place and object labels |
| Date / source metadata | 22–28 px | 500–600 | Date, location, archive, attribution |
| Subtitles | 44–54 px | 500–600 | Maximum 2 lines |

### Typography rules

- Keep large headlines editorial, not ornamental.
- Use old-style or high-contrast serif selectively; never sacrifice legibility for period atmosphere.
- Use small uppercase labels for archival metadata only.
- Keep body line-height around `1.3–1.5`; display line-height around `0.98–1.1`.
- Verify Vietnamese diacritics and historical names render correctly.

## 5. Canvas, composition, and safe area

- **Master canvas:** `1080 × 1920 px`, portrait `9:16`.
- Keep essential type, dates, map labels, and annotations approximately 90 px from left/right, 140 px from top, and 300 px from bottom.
- Confirm platform-specific overlay zones before export.
- Use a newspaper-like column rhythm without turning every frame into a literal newspaper page.
- Prefer asymmetrical layouts: artifact or archival image on one side, date/headline/caption on the other.
- Use full-frame historical imagery when it is compelling and legible; reserve paper backgrounds for explanatory overlays and transitions.
- Align dates, timeline labels, document captions, and source notes consistently.

## 6. Historical image and archival material direction

### Preferred material

- Authentic archival photographs and verified newsreel film footage with documented provenance (Library of Congress, National Archives, British Pathé, Gallica, Vietnam National Archives).
- Original historical newspaper clippings, broadsheets, headlines, and period periodicals.
- Primary historical artifacts: treaties, diplomatic letters, field dispatches, currency, medals, handwritten journals, and cartographic surveys.
- Museum artifact photography, architectural ruins, archaeological excavations, and verified historical monuments.
- Period artwork: contemporary woodblock prints, lithographs, paintings, and bronze engravings created during the era being examined.

### Image treatment (Vox Paper Collage)

- **Tactile Paper Cutouts:** Scanned historic black-and-white photographs isolated with crisp paper-cutout contours, cast against warm parchment (`#E8DFD0`) with subtle contact shadows (`rgba(0,0,0,0.12)`).
- **Newspaper Headline Crops:** Authentic scans of newspaper headlines layered diagonally or stacked, with key sentences illuminated by a translucent burgundy ink highlighter (`rgba(135, 63, 67, 0.25)`).
- **Cartographic Detail Crops:** High-resolution crops of period navigation or military maps, maintaining original paper grain and ink engravings.
- **Archive Provenance Metadata:** Every archival document or photo must display small, crisp source attribution (e.g., `National Archives, Ref. 1894-B`).

### Strict Anti-AI Guardrails (Do Not Use)

- **AI-generated fantasy historical figures & soldiers:** Absolutely ban Midjourney/Stable Diffusion plastic-skinned reenactments of historical figures, soldiers, monarchs, or civilians with fake cinematic lighting.
- **Invented historical records:** Never fabricate fake newspaper front-pages, bogus signatures, or fraudulent letters masquerading as primary sources.
- **Plastic period drama tropes:** Overly dramatic Hollywood-style 3D rendered battles, cinematic flame overlays, or fake smoke plumes.
- **Indiscriminate distressing:** Do not paste fake grunge, burn marks, or coffee stains over modern explanatory graphics.

## 7. Vox Paper Collage, Maps & 5-Evidence Props Toolkit

DẤU MỐC chuẩn hóa trọn bộ **5 Đạo cụ Bằng chứng Điều tra (Investigative Props Toolkit)** mang đậm DNA của Vox và Ken Burns:

1. **Prop 1: Băng dính Scotch Tape (`.scotch-tape`)**:
   - Chất liệu: Vàng nhạt bán trong suốt `linear-gradient(135deg, rgba(245, 235, 210, 0.78), rgba(240, 225, 195, 0.82))`, mép cắt răng cưa chân thực (`clip-path: polygon`).
   - **Quy tắc đính góc**: Băng dính PHẢI được lồng trực tiếp làm phần tử con (child) của thẻ tài liệu (báo chí, ảnh trinh sát) — tuyệt đối không để trôi nổi tự do.
   - Vị trí: Dán chéo ở hai góc trên: góc trên-trái xoay `-35°`, góc trên-phải xoay `+35°`. Nửa miếng đè lên mép tài liệu, nửa còn lại tràn ra mặt bàn.
   - Chuyển động: Đập dứt khoát xuống mặt giấy (`scale: 1.35 -> 1.0, opacity: 0 -> 1`) sau khi tài liệu tiếp đất 0.1s - 0.2s.

2. **Prop 2: Ghim đỏ 3D (`.red-pushpin`) & Sợi chỉ đỏ tác chiến (`.tactical-string`)**:
   - Thân ghim khối cầu đỏ thẫm 3D (`#DE2828` / `#871F23`), kim thép sáng bóng.
   - **Quy tắc định vị**: Cắm trực tiếp vào đúng tâm tọa độ địa lý căn cứ/chiến trường trên bản đồ (ví dụ: bệ tên lửa San Cristóbal Cuba), dập nảy cơ học (`back.out(2.5)`), phát ra 3 vòng sóng xung kích radar (`.radar-ring`).
   - **Sợi chỉ đỏ điều tra**: Đường nét đứt màu đỏ (`stroke: #873F43, stroke-width: 2.5px`) giật căng tức thì nối giữa hai vị trí cứ điểm chiến lược (ví dụ: Hạm đội Florida tới Cuba).

3. **Prop 3: Bút dạ quang Burgundy lem giấy (`.burgundy-highlighter`)**:
   - Sử dụng `mix-blend-mode: multiply` và sắc màu `rgba(135, 63, 67, 0.32)` thấm thấu tự nhiên vào thớ giấy (không dùng thanh chữ nhật phẳng lì).
   - Quét ngang dòng tít báo chí hoặc điều khoản hiệp ước (`scaleX: 0 -> 1`, `transformOrigin: left`, thời gian 0.8s - 1.2s).

4. **Prop 4: Kính lúp Tình báo Quang học (`.evidence-loupe`)**:
   - Thiết kế thực tế: Vành kim loại đúc nổi khối 3D màu antique gold (`#B18B55`), có tay cầm cán gỗ mun/đồng thau dài `180px` vươn ra góc chéo `45°` xuống phía dưới-phải màn hình.
   - Thị kính quang học: Phóng đại thực tế **2.2x** chi tiết tư liệu/hiện trường bên dưới, tích hợp vạch chữ thập trắc đạc quân sự (`crosshair reticle`), thước đo milimet trắc địa và vệt lóa phản quang cong (`loupe-glint`).
   - Chuyển động: Trượt vào rà quét qua tấm phim/bản đồ rồi khóa nét micro-settle (`scale: 1.05 -> 1.0`) vào đúng tâm mục tiêu.

5. **Prop 5: Vệt đen che tài liệu mật (`.redaction-bar`) & Dấu Giải Mật (`.declassified-stamp`)**:
   - Vệt mực đen kéo nhanh che các mật danh chiến dịch tối mật `[OPERATION CLASSIFIED]`.
   - Con dấu đỏ son `GIẢI MẬT // DECLASSIFIED` đóng dập xuống văn bản (`scale: 1.4 -> 1.0, rotation: -3deg`).

- **Mandatory Reconstruction Stamp:** Mọi bản đồ dựng lại hoặc sơ đồ 3D hiện đại không phải bản gốc lưu trữ bắt buộc phải có nhãn:
  ```
  [TÁI HIỆN MINH HỌA // AI RECONSTRUCTION]
  ```

---

## 8. Motion and transitions (Chuẩn mực Vox 2.5D)

Chuyển động trong DẤU MỐC tuân thủ nghiêm ngặt 3 nguyên lý điều tra của Vox và Ken Burns:

### A. Continuous Camera Drift & 3-Layer Parallax (Zero Static Frames)
- **Quy tắc Zero Static Frames:** Mỗi Scene bắt buộc phải nằm trong một `.camera-stage` vận hành camera slow push-in liên tục (`scale: 1.0 -> 1.055`, trôi Y `0 -> -20px`) trong suốt 7–9 giây của scene. Tuyệt đối không để khung hình bị "chết tĩnh" sau khi xuất hiện.
- **Phân tầng chiều sâu 2.5D**:
  - **Background Layer (Parallax 0.5x–0.6x):** Nền bàn gỗ, giấy parchment, lưới tọa độ quân sự trôi chậm.
  - **Middle Layer (Parallax 1.0x):** Tài liệu lưu trữ, trang báo cổ, ảnh hiện trường, bản đồ chiến sự.
  - **Foreground Layer (Parallax 1.4x–1.5x):** Đạo cụ bằng chứng (Băng dính Scotch, ghim đỏ 3D, kính lúp điều tra, con dấu) trôi nhanh hơn và đổ bóng tiếp xúc sâu (`filter: drop-shadow`).

### B. Tactile Paper Placement (Cơ chế Thả Giấy Ma Sát Thực)
- Tài liệu rơi xuống bàn dứt khoát (`y: -50px -> 0`, thời gian 0.35s - 0.4s, `ease: "power2.out"`).
- Kết hợp ngay sau đó là chuyển động **micro-settle** (nảy nhẹ 2-3px và ổn định trong 0.12s) với góc nghiêng ngẫu nhiên tự nhiên (`-1.5°` đến `+1.5°`), tái hiện cảm giác thả tư liệu lên bàn làm việc.

### C. Motion constraints
- Tránh chuyển động lướt kỹ thuật số mượt mà vô hồn (digital smooth glide); tư liệu phải có quán tính, ma sát và trọng lượng giấy.
- Không dùng hiệu ứng xoay 3D lòe loẹt, glitch số hóa, hoặc tia laser sci-fi.
- Mọi chuyển động phải tôn trọng tính trang nghiêm của sự kiện và nhân vật lịch sử.

## 9. Subtitle and on-screen text system

- Use sentence-level subtitles, maximum two lines.
- Default to dark `ink` text (`#292624`) on a warm-white or parchment plate (`#FAF8F3`).
- On dark full-bleed archival footage, use crisp white text on a deep tone plate (`#211D1B`).
- Highlight decisive dates, turning points, or historical figures in `burgundy` (`#873F43`); use `antique-gold` (`#B18B55`) for treaties or artifact metadata.
- Keep source credits and archive callouts visually separated from spoken subtitles.
- Never let subtitles obscure faces in historical photos, treaty signatures, or map routes.
- Maintain consistent subtitle placement within the lower safe region.

## 10. Reusable scene patterns

1. **Historical hook:** a powerful image or object with a short editorial question or claim.
2. **Time and place:** date, location, and a map or contextual archival image.
3. **Primary evidence:** original document, photograph, object, or credible source excerpt.
4. **Sequence:** a timeline or map that explains how events unfolded.
5. **Decision and consequence:** a person, institution, invention, or turning point with a clear causal relationship.
6. **Legacy:** a present-day image or concise closing thought connecting the event to its longer-term significance.

Do not force every story into all six patterns. The historical evidence and narrative should determine the sequence.

## 11. Historical integrity and source handling

- Do not fabricate quotations, dates, people, documents, borders, or archival evidence.
- Identify a reconstruction or reenactment when a viewer could reasonably mistake it for real historical footage.
- Distinguish contested interpretations from established facts in wording and visual treatment.
- Avoid implying that a generic image depicts a named person or exact event unless it is verified.
- Preserve uncertainty where historical scholarship is divided.
- Keep image attribution and source information available in production metadata and on-screen where useful.

## 12. Anti-patterns

- **AI-generated historical figures:** Never use Midjourney or Stable Diffusion fantasy portraits of historical leaders, soldiers, or victims with smooth plastic skin and artificial cinematic lighting.
- **Fabricated archival evidence:** Inventing fake newspaper front-pages, bogus signatures, or fraudulent telegrams.
- **Indiscriminate sepia & grunge:** Slapping sepia filters, fake burns, coffee stains, and heavy vignette shadows across every frame.
- **Hollywood CGI war trailers:** 3D rendered explosions, flying bullet tracers, and dramatic movie-trailer text effects.
- **Generic timeline clutter:** Stacking dozens of tiny unreadable dates on one vertical screen.
- **Unlabeled AI reconstructions:** Presenting modern reconstructions without the mandatory `[TÁI HIỆN MINH HỌA // AI RECONSTRUCTION]` stamp.

## 13. Hyperframe implementation guidance

- Create reusable **Vox paper collage compositions**: archival newspaper headline collage, torn-paper portrait cutout with parchment mount, animated map route sequence, treaty document highlighter excerpt, and historical legacy closing.
- Structure layouts with paper layers (`z-index`), tactile rotation offsets (`-2deg to 2deg`), and soft contact shadows (`box-shadow: 0 4px 16px rgba(0,0,0,0.12)`).
- Tokenize `paper` (`#FAF8F3`), `parchment` (`#E8DFD0`), `ink` (`#292624`), `burgundy` (`#873F43`), `antique-gold` (`#B18B55`), and `rule` (`#DED8CF`).
- Implement DrawSVG animated pencil route vectors on high-res cartographic image canvases.
- Keep source credits, archive references, and reconstruction stamps as editable text layers.
- Do not bake paper-cutout text or headlines into raster flattened assets.

## 14. Quality checklist

- [ ] Output is vertical `1080 × 1920` (`9:16`).
- [ ] Essential text, dates, and paper clippings respect safe areas (Left/Right 90px, Top 140px, Bottom 300px).
- [ ] Graphic style adheres to **Style 6 — Vox Paper Collage & Archival Documentary** on tactile `paper` (`#FAF8F3`) / `parchment` (`#E8DFD0`).
- [ ] **Zero Static Frames Rule**: Mọi scene đều có camera 2.5D push-in liên tục (`1.0 -> 1.055`) và phân tầng 3 lớp (Background 0.5x, Midground 1.0x, Foreground 1.4x).
- [ ] **Tactile Paper Placement**: Tài liệu thả rơi dứt khoát có độ trễ ma sát giấy và micro-settle (`-1.5°` đến `+1.5°`).
- [ ] **5-Evidence Props Standard**:
  - Băng dính Scotch dán chuẩn xác ở 2 góc trên (`-35°` và `+35°`), một nửa đè lên tài liệu, một nửa tràn ra nền.
  - Ghim đỏ 3D cắm trực tiếp vào đúng tâm tọa độ bản đồ, kèm sợi chỉ đỏ căng nối cứ điểm chiến lược.
  - Bút dạ quang Burgundy sử dụng `mix-blend-mode: multiply` quét thớ mực tự nhiên.
  - Kính lúp điều tra có vành đồng 3D, cán gỗ mun/đồng dài chĩa góc `45°`, phóng đại quang học thực tế **2.2x** kèm tâm ngắm trắc đạc quân sự.
  - Vệt đen che mật danh và con dấu đỏ son giải mật văn bản.
- [ ] Archival photos use authentic B&W or historical color scans with paper-cutout framing and contact shadows.
- [ ] Battle/voyage maps feature animated pencil route lines (`stroke: #873F43`) across authentic cartography.
- [ ] Any modern recreation carries the prominent stamp `[TÁI HIỆN MINH HỌA // AI RECONSTRUCTION]`.
- [ ] Subtitles do not cover historical faces, signatures, or document passages.
- [ ] **Strict Anti-AI Verification:** Strictly 100% authentic archival records or verified historical artifacts; zero AI fantasy historical figures or plastic faces.
