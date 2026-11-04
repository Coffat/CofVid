# MẠCH SỐ — Video Design System

> **COFFAT MEDIA · Channel Design Specification**  
> Version 2.2 · Format: vertical documentary / explainer video · Aspect ratio: 9:16  
> **Official Approved Style: Neo-Brutalist Tactile Bento / Developer Motion**  
> **HUD Architecture: Cinematic Scene-Driven HUD (Option 4 Approved)**  
> **Layout & Motion Framework: 5 Context-Driven Archetypes Suite (2026 Developer Motion Standard)**

## 1. Purpose and scope

MẠCH SỐ explains technology, artificial intelligence, algorithms, software architecture, infrastructure, and the computational systems shaping the digital world.

This document is the authoritative visual source of truth for MẠCH SỐ video production. It governs storyboards, Hyperframes HTML compositions, GSAP motion choreography, persistent HUD elements, cards, and typography.

**This is a video design system, not a website or app design system.** Do not create web dashboards, landing pages, channel banners, or social thumbnails from this specification.

### Design direction

- **Primary Style:** **Neo-Brutalist Tactile Bento / Developer Motion** (High-energy, tangible developer craft with tactile physics).
- **Mood:** hyper-clear, architectural, tactile, authoritative, fast-paced, high-density, and evidence-led.
- **Visual thesis:** Complex computing architecture should not be an abstract dark void; it should be tangible, structured, delightfully tactile, and immediately comprehensible.
- **Primary principle:** Vibrant lavender canvas (`#CBC3FA`) with a subtle technical dot-grid, tactile bento cards with bold 3.5px ink borders (`#181826`), bold 3D purple drop shadows (`0 10px 0 #9D91E8`), crisp Inter & IBM Plex Mono typography, and a dynamic **Cinematic Scene-Driven HUD system** (Zero-HUD hooks, minimal terminal breadcrumbs, and contextual benchmark battle HUDs).

---

## 2. Core visual principles

1. **Tangible Neo-Brutalist Bento Structure.** Every concept, code snippet, system node, or metric lives inside a tactile bento card with a thick 3.5px border (`#181826`) and signature solid shadow (`0 10px 0 #9D91E8`).
2. **Lavender Dot-Grid Canvas.** The master canvas is anchored in signature lavender (`#CBC3FA`) overlaid with an engineering dot-grid (`radial-gradient(#ABA0EE 2.2px, transparent 2.2px)`).
3. **Cinematic Scene-Driven HUD (Option 4 Architecture).** Không dùng thanh topbar cố định gò bó xuyên suốt video. HUD xuất hiện và biến hóa linh hoạt dựa trên nhịp điệu kịch bản và vai trò của từng cảnh (Scene Archetypes):
   - **Hook Scenes (Cảnh mở đầu / Giữ chân 3s):** **Zero HUD**. Mép trên hoàn toàn thoáng đãng, không có banner hay thanh bar nào cản trở thị giác; chữ tiêu đề cực đại và đồ họa chính bắt đầu ngay từ `y=160`.
   - **Deep-Dive / Breakdown Scenes (Phân tích kỹ thuật / Code / Sơ đồ):** **Micro Breadcrumb & Step Pill** tại `y=160`. Mép trái `x=64` hiển thị terminal breadcrumb monospace (`● sys/pipeline.ts // PHASE 02: PARSER`), mép phải `right=64` hiển thị pill tiến độ nhỏ gọn (`2/6`). Nội dung bắt đầu từ `y=240` (giải phóng thêm **+192px** chiều dọc so với chuẩn cũ).
   - **Benchmark / Climax Battle Scenes (So găng hiệu năng / Đo đạc / Sự cố):** **Full Battle Drop-down HUD** xuất hiện cơ học tại `y=160..300` (Dual Gauge Before/After, Latency Counter hoặc Incident Alert Strip). Nội dung bắt đầu từ `y=360`. Chuyển động animation biến đổi linh hoạt tùy ngữ cảnh kịch bản (mechanical slam, split slide-in, hoặc shake pulse).
   - **Outro Scenes (Kết thúc / Kêu gọi hành động):** HUD thu gọn biến thành thẻ Bento Signature kèm nút CTA nảy nhẹ.
4. **Interactive Tactile Physics & Developer Interactions.** Thay vì lạm dụng con trỏ chuột (`#global-cursor`) như một công cụ chỉ điểm đơn điệu, Mạch Số sử dụng bộ **6 Developer Interaction Primitives** (Keycombo HUD, Line Spotlight/Highlighter, Framing Brackets, Laser Scanner, Bus Pulse, Stamp Slam) để dẫn dắt ánh nhìn và kích hoạt phản hồi xúc giác. Chuột ảo chỉ được dùng khi mô phỏng thao tác người dùng trên giao diện web/app thực tế (tối đa 1-2 lần/video).
5. **Purposeful Accent Encoding.**
   - `mint-green` (`#10B981` / surface `#D1FAE5`) signifies optimal performance, verified tokens, sub-second execution, and active nodes.
   - `coral-red` (`#FF4757` / surface `#FFE1E4`) signifies bottlenecks, parsing crashes, timeouts, and latency spikes.
6. **Disciplined Modular Grid (8px snap) & Dynamic Clearance.** Safe margins at 64px left/right. Content zone clearance (`y_start`) adapts dynamically theo 3 tầng HUD:
   - Hook: `y = 160 … 1680` (1520px canvas tối đa).
   - Deep-Dive: `y = 240 … 1680` (1440px canvas rộng rãi).
   - Benchmark Battle: `y = 360 … 1680` (1320px canvas tập trung).  
   Grid cards are 456px wide (columns at `x=64` and `x=560`) with standard 32px gaps. Full-width cards are 952px wide.
7. **Tangible Evidence Over Sci-Fi Hallucination.** Prefer real terminal logs, authentic benchmark cards, documented architecture topologies, and crisp code snippets over fake floating holograms.
8. **Authentic Vector Marks Over Ad-hoc SVG Diagrams (`brand_icon_tool`).** Always resolve official corporate/technology vector marks (`github`, `docker`, `aws`, `cloudflare`, `python`, `react`, `kubernetes`, `linux`, `postgres`, `redis`, etc.) and UI icons (`shield`, `terminal`, `database`, `star`, `check`) using `brand_icon_tool`. Strictly ban hand-coding custom SVG diagrams/logos that look distorted, amateurish, or like AI hallucinations. SVG is reserved strictly for structural UI: process arrows (`stroke-width 8px`), bus connectors, and window chrome.
9. **Monumental & High-Legibility Image Framing.** Never constrain images, incident screenshots, or architecture diagrams into cramped sub-400px boxes. Images must be prominently featured in designated Media Bento Cards (`952 × 600–720px` in Hero layout, `952 × 960px` in Showcase layout, or `456 × 780px` in Dual Compare) with crisp `3.5px` borders, authentic brand badges, and clear visual hierarchy so viewers on mobile screens (9:16) can inspect every detail clearly.
10. **Hard Quality Gate — Real Visual Assets Mandate.** Scene Plan must declare at least 1 real visual asset (`brand_icon_tool` vector logos, OpenGraph / UI screenshots, dynamic SVG architecture diagrams, or code snippets) for every deep-dive scene. The `assets` stage MUST download/generate them into `assets/images/` before advancing to `compose`. Never render deep-dive scenes with empty placeholder boxes or fake mock graphics.

---

## 3. Color system

### Core color tokens

| Token | CSS Variable | Hex | Role |
|---|---|---|---|
| `bg-lavender` | `--bg-lavender` | `#CBC3FA` | Primary master canvas background |
| `dot-grid` | — | `#ABA0EE` | 40px × 40px radial dot-grid pattern (opacity: 0.45) |
| `shadow-purple` | `--shadow-purple` | `#9D91E8` | Signature solid drop shadow (`0 10px 0 #9D91E8`) |
| `surface-white` | `--surface-white` | `#FFFFFF` | Primary card surface; clean contrast on lavender |
| `surface-sand` | `--surface-sand` | `#F3EBDD` | Vintage Technical Sand; HUD Micro Breadcrumbs, Step Pills, Battle HUD, and retro tactile cards |
| `surface-dark` | `--surface-dark` | `#181826` | Dark card surface, 3.5px borders, text ink |
| `mint-green` | `--mint-green` | `#10B981` | Positive accent; sub-100ms latency, success stamps, verification |
| `mint-surface` | `--mint-surface` | `#D1FAE5` | Mint card fill for verified nodes and benchmark wins |
| `coral-red` | `--coral-red` | `#FF4757` | Warning accent; bottlenecks, crashes, high latency |
| `coral-surface` | `--coral-surface` | `#FFE1E4` | Coral card fill for error alerts and incident logs |
| `purple-accent` | `--purple-accent` | `#7A6BE0` | Monospace tags, sub-headings, section identifiers |
| `deco-light` | — | `#ECE8FF` | Large background vector pluses, rings, and decorative blobs |

### Color usage rules

- **Canvas Rule:** The canvas is strictly `#CBC3FA` with dot grid. Never use pitch black or dark grey canvas.
- **HUD & Breadcrumb Rule:** Mọi thành phần HUD (Micro Breadcrumb, Step Pill, Battle HUD) sử dụng nền `#F3EBDD` (Vintage Technical Sand) với viền `3px solid #181826`, bóng tím `0 6px 0 #9D91E8` và chữ đen `#181826`. Tuyệt đối KHÔNG dùng nền đen kịt `#181826` cho HUD để tránh cảm giác nặng nề trên nền tím Lavender.
- **Card Rule:** Bento cards use `#FFFFFF`, `#F3EBDD` (sand), `#181826`, `#D1FAE5` (mint), or `#FFE1E4` (coral). Every card must have `border: 3.5px solid #181826` and `box-shadow: 0 10px 0 #9D91E8`.
- **Text Rule:** On white and sand cards, text is `#181826`. On dark cards, text is `#FFFFFF`. Key numbers use `#10B981` or `#FF4757`.
- **Anti-AI Palette Rule:** Strictly ban glowing cyan-magenta neon, holographic iridescent gradients, and blurred glowing edges.

---

## 4. Typography

### Type families

| Role | Font Family | Weights | Guidance |
|---|---|---|---|
| Headlines, Bento Titles, Pill Badges | **Inter** | 700, 800, 900 | Tight letter-spacing (`-0.02em`), uppercase for badges |
| Code Snippets, Token IDs, Latency, Metrics | **IBM Plex Mono** | 600, 700 | Crisp tabular figures, technical authenticity |

### Type scale (1080 × 1920 reference)

| Level | Size | Weight | Line Height | Usage |
|---|---|---|---|---|
| Hero Metric / Number | 96–128 px | 900 | 1.0 | Speedup multiples, latency numbers (`0.48s`, `70ms`) |
| Bento Title / Strong Label | 48–56 px | 900 | 1.15 | Prompt inputs, main card headers |
| Standard Label / Stat Title | 34–40 px | 800 | 1.2 | Card labels, descriptions (max 5 words) |
| Monospace Tag / Eyebrow | 28–34 px | 700 | 1.0 | `INPUT`, `pgvector // RAG`, `TypeScript SDK` |
| Banner Kinetic Words | 38 px | 900 | 1.0 | Top HUD banner phrases |
| Pill Badges | 36–44 px | 900 | 1.0 | Callouts, action buttons (`Gửi ➤`, `+ THEO DÕI`) |

---

## 5. Canvas layout & composition

- **Master dimensions:** `1080 × 1920 px` (portrait `9:16`).
- **Safe margins:** Left/Right **64px**, Top **160px**, Bottom **240px**.
- **8px Modular Grid:** Card widths:
  - Full width card: **952px** (left: 64px)
  - 2-column bento card: **456px** (col 1: left 64px, col 2: left 560px, gap: 32px)
  - 3-column / doc icon card: **240px** to **280px**

### Cinematic Scene-Driven HUD Specifications (3-Tier Dynamic Clearance)

| Scene Archetype | HUD Elements | Clearance (`y_start`) | Visual Guidance |
|---|---|---|---|
| **Tier 1: Hook Scene** | **Zero HUD** (None) | **`y ≥ 160px`** | Mép trên thoáng hoàn toàn, không có banner. Hero Bento hoặc tiêu đề Typography cực đại đặt ngay tại `y=160..300` để giữ chân người xem 3s đầu. |
| **Tier 2: Deep-Dive / Code** | **Micro Breadcrumb + Step Pill** | **`y ≥ 240px`** | Nền Be Cát `#F3EBDD`, viền 3px đen, shadow tím `0 6px 0 #9D91E8`. Góc trái `x=64, y=160`: Terminal tag (`● sys/pipeline.ts // PHASE 02: PARSER`). Góc phải `right=64, y=160`: Step pill (`2/6`). Thẻ Bento phân tích bắt đầu tại `y=240`. |
| **Tier 3: Benchmark / Climax** | **Full Battle HUD / Incident Strip** | **`y ≥ 360px`** | Nền Be Cát `#F3EBDD` (hoặc đỏ `#FFE1E4` khi sự cố), viền 3.5px đen. Bộ Dual Gauge HUD hoặc Incident Strip hạ cánh cơ học tại `y=160..300`. Thẻ so sánh đối đầu bắt đầu tại `y=360`. |

### 5 Context-Driven Scene Archetypes (Ngũ Phân Hệ Ngữ Cảnh)

MẠCH SỐ phân loại cấu trúc khung hình và chuyển động tương ứng dựa trên **5 Ngữ Cảnh Nội Dung Cốt Lõi**:

1. **Archetype 1 — Product & AI Tool Showcase (`product_tool_showcase`):**
   - **Mục đích:** Giới thiệu công cụ AI, SaaS, trình soạn thảo, tính năng sản phẩm mới.
   - **Bố cục chuẩn:**
     - Hero App Window (`952 × 600–720px` đặt tại `y=240`): Khung cửa sổ macOS dots (`● ● ●`), thanh địa chỉ URL (`app.domain.com`), nút bấm tương tác CTA.
     - Bottom Killer Features (`2 cột 456 × 400px` tại `y=900..1040`): Liệt kê 2 tính năng sát thủ với icon chính hãng từ `brand_icon_tool`.
   - **Chuyển động:** Virtual Cursor (`#global-cursor`) lướt vào click nút Action (`power2.inOut`), kích hoạt vòng gợn sóng xanh mint (`#click-ripple`). Khung mã nguồn/app trượt mở tức thì (slide reveal).

2. **Archetype 2 — GitHub Repo & Open Source Deep-Dive (`github_repo_deepdive`):**
   - **Mục đích:** Mổ xẻ kho lưu trữ mã nguồn mở, repo hot, quy trình cài đặt và chạy thử.
   - **Bố cục chuẩn:**
     - Header Repo (`952 × 260px` tại `y=240`): Logo GitHub Octocat chính hãng, tên repo (`owner/repo-name`), badge License (MIT/Apache), và ngôi sao vàng lớn.
     - Terminal IDE Window (`952 × 460px` tại `y=540`): Dòng lệnh cài đặt (`pnpm dlx ...` hoặc `git clone`), dòng log output biên dịch thành công màu xanh mint.
     - Khung Demo Preview (`952 × 520px` tại `y=1040`): Ảnh hoặc video demo thật lấy trực tiếp từ GitHub OpenGraph metadata hoặc README của repo (bảo đảm tính xác thực 100%, không bịa đặt).
   - **Chuyển động:** **GitHub Star Explosion**: Ngôi sao vàng (`★`) bùng nổ nảy lớn (`scale: 1.7 -> 1.0`), counter số stars nhảy từ 0 lên số sao thật. Terminal gõ phím từng ký tự (Typewriter `_`) dồn dập.

3. **Archetype 3 — Architecture Theory & Data Pipeline (`architecture_theory`):**
   - **Mục đích:** Giải mã nguyên lý ngầm, thuật toán phân tán, RAG pipeline, cơ chế KV-cache.
   - **Bố cục chuẩn:**
     - 3 Tầng Node Kiến Trúc nối nhau bằng đường bus mạch điện đen đậm (`stroke-width: 8px`, `#181826`).
     - Node Input (`y=240`), Node Xử lý trung gian (`y=620`, ví dụ pgvector/Cache), Node Output (`y=1000`, LLM Generator).
     - Thẻ Telemetry Monitor chân trang (`952 × 200px`): Đo lường độ trễ (Latency ms) và thông lượng (Throughput req/s).
   - **Chuyển động:** **Tactile Data Packet Flow**: Hạt tròn xung dữ liệu viền đen bắn vèo dọc đường dây bus. Khi chạm vào Node tiếp theo, Node nảy cơ học (`scale: 1.04 -> 1.0`) và viền chớp sáng xanh mint `✓ CACHE HIT`. Hạt tiếp tục bắn sang Node kế tiếp kích hoạt luồng token stream.

4. **Archetype 4 — Benchmark & Performance Battle (`benchmark_fact_battle`):**
   - **Mục đích:** So găng tốc độ, đối đầu kiến trúc Before vs After, sự thật kỹ thuật giật mình.
   - **Bố cục chuẩn:**
     - Full Battle Drop-down HUD màu Be Cát `#F3EBDD` tại `y=160`: So sánh hai chỉ số Before/After và badge `VS`.
     - Split Dual Compare (`2 cột 456 × 840px` tại `y=320`): Cột Trái đỏ san hô `#FFE1E4` (nghẽn cổ chai) đối đầu Cột Phải xanh mint `#D1FAE5` (đã tối ưu).
     - Thẻ Kết Luận khổng lồ (`952 × 340px` tại `y=1210`): Số liệu nhân bội cực đại `96–128px` (`78x FASTER`, `-85% MEMORY`).
   - **Chuyển động:** Hai cột lao vào từ hai bên va chạm cơ học nảy vật lý. Đồng hồ số counter quay tít như công tơ mét rồi phanh kịch kim (snappy brake). Con dấu `✓ BENCHMARK VERIFIED` dập xuống xoay `-4°`.

5. **Archetype 5 — Incident Post-Mortem & Digital Forensics (`incident_post_mortem`):**
   - **Mục đích:** Mổ xẻ sự cố sập mạng toàn cầu (Cloudflare, AWS, CrowdStrike), phân tích lỗi OOM/Crash.
   - **Bố cục chuẩn:**
     - Dải Alert Strip đỏ rực tại `y=160` (`952 × 80px`, màu `#FF4757`, chữ trắng): Mã lỗi khẩn cấp (`HTTP 502`, `KERNEL PANIC`).
     - Cửa sổ Crash Console (`952 × 640px` tại `y=280`): Đoạn stack trace, coredump, dòng code gây lỗi.
     - Thẻ Đo Lường Thiệt Hại (`952 × 360px` tại `y=960`): Số lượng máy tính/traffic bị tê liệt và tổng thiệt hại tài chính.
   - **Chuyển động:** Rung lắc chấn động cơ học (Micro-shake `x: -8..8px`). Hàng chục dòng log tuôn trào dồn dập rồi khựng lại ở dòng mã lỗi màu đỏ rực. Con dấu đỏ `✓ ROOT CAUSE VERIFIED` dập xuống khẳng định nguyên nhân gốc rễ.

---

## 6. Motion and animation rules (Developer Motion & Interaction Suite 2026)

### A. Bộ 6 Developer Interaction Primitives (Dẫn dắt thị giác & Kích hoạt hành động)

Thay vì lạm dụng con trỏ chuột, Mạch Số sử dụng 6 chuyển động tương tác mang đậm tư duy kỹ thuật của dân công nghệ chuyên nghiệp:

1. **Keycombo HUD (`⌘K`, `Enter`, `Tab`, `Esc`):**
   - Phím bấm vật lý cơ học (`border: 2.5px solid #181826`, bóng nổi `0 5px 0 #9D91E8`).
   - Khi trigger hành động/lệnh: phím lún xuống cơ học (`y: +4px`, bóng thu về `0 1px 0`, viền chớp sáng `#10B981` trong 0.12s) rồi nảy lại `back.out(2.0)`.
   - Dùng khi: Chạy terminal, gọi action, mở command palette, kích hoạt pipeline.

2. **Highlighter Sweep & Line Spotlight (Khóa thị giác theo giọng đọc):**
   - Vệt bút dạ quang bán trong suốt (`rgba(16, 185, 129, 0.25)` cho tối ưu/thành công hoặc `rgba(255, 71, 87, 0.25)` cho lỗi/cảnh báo) quét từ trái sang phải (`scaleX: 0 -> 1`, `transformOrigin: left center`, duration: 0.35s).
   - Đồng thời kích hoạt **Selective Focus**: Dòng code/thẻ đang giải thích sáng viền Mint và scale nhẹ `1.02x`, các dòng/thẻ xung quanh mờ xuống `opacity: 0.40`.

3. **Framing Brackets / HUD Reticle (Khóa mục tiêu cơ khí):**
   - 4 góc ngắm cơ khí (L-shape corner brackets viền 3px `#181826`) từ ngoài phóng vào ôm sát khung viền bento card cần nhấn mạnh (`scale: 1.15 -> 1.0`, `opacity: 0 -> 1`, `power2.out`, 0.25s).
   - Dùng khi: Muốn thu hút 100% sự chú ý của người xem vào 1 module, tham số hoặc card cụ thể mà không cần chỉ trỏ chuột.

4. **Laser Scanline / Radar Sweep (Quét giải mã & Phân tích):**
   - Dải tia sáng laser mảnh viền gradient chớp sáng quét dọc từ trên xuống dưới qua card mã nguồn, sơ đồ hoặc bảng dữ liệu (`duration: 0.6s–0.8s`, `power1.inOut`).
   - Các dòng chữ/token khi tia laser quét qua sẽ chuyển màu highlight trong tích tắc.
   - Dùng khi: Quét lỗ hổng bảo mật, biên dịch code, giải mã cấu trúc file, benchmark telemetry.

5. **SVG Data Bus Pulse & Node Bounce (Luồng dữ liệu thực thể):**
   - Đường bus mạch điện đen đậm 8px (`stroke-width: 8px`, `#181826`) vẽ bằng `stroke-dashoffset` trong 0.45s (`power2.out`).
   - Hạt xung dữ liệu viền đen (`.pulse-dot`) bắn dọc theo dây với gia tốc `power2.inOut`.
   - Khi hạt chạm vào node tiếp theo, node nảy nhẹ cơ học (`scale: 1.05 -> 1.0` trong 0.18s) kèm viền chớp xanh mint để báo hiệu tiếp nhận dữ liệu.

6. **Mechanical Stamp Slam & Odometer Counter (Chốt hạ kết quả):**
   - **Stamp Slam:** Con dấu kiểm định đỏ/mint (`✓ BENCHMARK VERIFIED`, `✓ ROOT CAUSE FOUND`) dập rầm rộ xuống với `scale: 1.6 -> 1.0`, góc xoay `-3deg`, lực nảy `back.out(2.2)`.
   - **Mechanical Odometer:** Số liệu đếm nhảy tít như đồng hồ cơ khí và phanh dứt khoát tại giá trị thật bằng `expo.out` (1.2s–1.6s).

---

### B. Quy tắc Kiểm soát Con Trỏ Chuột Ảo (Strict Virtual Cursor Policy)

- ❌ **CẤM LẠM DỤNG:** Tuyệt đối không dùng `#global-cursor` như chiếc gậy chỉ bảng để lượn qua lượn lại, trỏ vào tiêu đề, bullet point, hoặc click vào mọi thẻ card trong video.
- ✅ **NGỮ CẢNH HỢP LÝ DUY NHẤT:** Con trỏ chuột chỉ được dùng khi mô phỏng **thao tác người dùng thực sự trên giao diện web/desktop** (ví dụ: người dùng nhập prompt rồi click nút Gửi trên giao diện web, hoặc kéo thanh trượt Slider A/B).
- ⏱️ **TẦN SUẤT TỐI ĐA:** Tối đa 1-2 lần trong toàn bộ một video dài 60-90 giây. Tất cả các cảnh thuật toán, kiến trúc, terminal, repo, benchmark đều dùng bàn phím, laser scan, hoặc bus pulse.

---

### C. Bảng Ma Trận Mục Đích Nhận Thức (Cognitive Purpose Motion Matrix)

Để AI Agent chọn animation một cách **thông minh, hợp lý và không máy móc**, Agent phải đối chiếu mục đích truyền đạt của câu thoại/cảnh với ma trận sau:

| Ý Đồ Kịch Bản & Trọng Tâm Nhận Thức | Animation Đề Xuất (Recommended Primitive) | Phản Hồi Thị Giác & Xúc Giác | Điều Cần Tránh (Anti-Pattern) |
|---|---|---|---|
| **Khởi chạy lệnh / Kích hoạt tool / Chạy build** | **Keycombo HUD** (`⌘K`, `Enter`, `Tab`) hoặc **Typewriter Terminal** | Phím cơ lún xuống, viền chớp sáng, log tuôn trào theo nhịp gõ | ❌ Không dùng chuột bay vào click nút ảo |
| **Phân tích chi tiết 1 dòng code / từ khóa kỹ thuật** | **Highlighter Sweep + Line Spotlight** | Vệt dạ quang quét ngang, dòng chọn scale 1.02x, nền xung quanh mờ 40% | ❌ Không phóng to giật cục cả khung hình |
| **Giải thích cơ chế ngầm / Gửi token / API Request** | **SVG Bus Pulse + Node Micro-Bounce** | Hạt xung điện bắn dọc bus 8px, node nhận dữ liệu nảy nhẹ | ❌ Không để mũi tên tĩnh không chuyển động |
| **Rà soát sự cố / Debug lỗi / Quét lỗ hổng** | **Laser Scanline / Radar Sweep** | Tia quét quang học quét dọc khối code/file, dừng ở dòng lỗi | ❌ Không dùng chuột rê tìm dòng lỗi |
| **Cô lập & Khóa tiêu điểm vào 1 module hệ thống** | **Framing Brackets (HUD Reticle)** | 4 góc ngắm cơ khí ôm sát viền thẻ bento với tốc độ giật nhanh | ❌ Không vẽ vòng tròn nguệch ngoạc |
| **Chứng thực kết quả / Số liệu benchmark thần tốc** | **Mechanical Odometer + Stamp Slam** | Số quay tít phanh gấp `expo.out`, con dấu dập nghiêng `-3°` | ❌ Không dùng fade-in chữ thông thường |
| **Tương tác trực tiếp trên giao diện sản phẩm SaaS/Web** | **Virtual Cursor Click + Mint Ripple** | Chuột lướt nhẹ click nút CTA, vòng sóng gợn xanh mint tỏa ra | ❌ Không dùng chuột nếu không phải ngữ cảnh web/app |

*Lưu ý cho AI Agent:* Không cấm lặp lại animation nếu 2 cảnh liên tiếp cùng có mục đích nhận thức giống nhau (ví dụ: 2 cảnh cùng so sánh thông số benchmark thì đều có thể dùng Odometer/Stamp). Tiêu chuẩn đánh giá cao nhất là **Tính Hợp Lý Nhận Thức (Cognitive Fitness)** — chuyển động phải phục vụ người xem hiểu nội dung nhanh nhất.

---

### D. Nền tảng Chuyển Động Liên Tục (Continuous Motion Foundation)

- **Snappy Card Reveal:** Bento cards xuất hiện bằng `fromTo({ opacity: 0, scale: 0.97, y: 35 }, { opacity: 1, scale: 1.0, y: 0, duration: 0.28, ease: "cubic-bezier(0.16, 1, 0.3, 1)" })`. Triệt tiêu hoàn toàn cảm giác rung giật hoạt hình.
- **Continuous Camera Slow-Drift:** Toàn bộ camera wrap duy trì lực đẩy siêu chậm `scale: 1.0 -> 1.025x` xuyên suốt cảnh để video luôn có sinh khí, tối ưu retention.
- **Dynamic Camera Pan & Tilt:** Camera trượt nhẹ nhàng bám theo đối tượng đang được giọng đọc thuyết minh (pan từ breadcrumb xuống code block hoặc tilt giữa 2 cột đối đầu).
- **Seamless Tech Wipe / Zoom-Through:** Chuyển cảnh bằng vệt cắt kỹ thuật cơ khí hoặc zoom xuyên tâm node dữ liệu.

---

## 7. Anti-patterns (Strictly prohibited)

- ❌ **Lạm dụng trỏ chuột & hội chứng 'Gậy chỉ bảng' (Cursor Overuse & Pointing Stick Syndrome):** Nghiêm cấm dùng con trỏ chuột lượn lờ chỉ từng dòng chữ, bullet point, hoặc click vào mọi thẻ một cách vô nghĩa. Áp dụng đúng Bảng Ma trận Mục đích Nhận thức (chuột chỉ dùng tối đa 1-2 lần cho giao diện web/desktop thực tế).
- ❌ **Handmade SVG diagrams & fake logos:** Strictly FORBIDDEN to hand-code SVG paths to draw company logos or complex custom diagrams. Always use `brand_icon_tool` for authentic corporate marks and clean UI icons. Hand-authored SVG is allowed only for directional arrows, connectors, and window dots.
- ❌ **Cramped & tiny image boxes:** Never place architecture screenshots, incident graphs, or news photos in boxes narrower than 450px or shorter than 260px. Images must be large, high-contrast, and instantly readable on vertical 9:16 phone screens.
- ❌ **Dark space / blue-black void canvas:** Do not use `#111820`, `#0C1017`, or dark-grey backgrounds for the master video canvas. The canvas is strictly Lavender `#CBC3FA`.
- ❌ **Thin 1px wireframes:** Do not use faint 1px grey borders. Mach So uses bold 3.5px solid `#181826` borders.
- ❌ **Generic AI gradients:** Absolutely no cyan-purple neon glowing glows, rainbow edges, or blurry drop shadows.
- ❌ **Floating 3D objects & holograms:** No floating 3D cubes, rotating polyhedra, or fake sci-fi HUDs.
- ❌ **Cluttered, overlapping layouts:** Never place cards on top of each other (except intentional stamps, cursor, and live badges). Everything respects the 8px grid and dynamic content zones (`y ≥ 160 / 240 / 360`).
- ❌ **Long text paragraphs:** No paragraphs of text. Maximum 5 words per label, large bold numbers, and high-impact typography.

---

## 8. Quality checklist

- [ ] Output is vertical `1080 × 1920 px` (`9:16`).
- [ ] Canvas is Lavender `#CBC3FA` với 40px dot-grid pattern.
- [ ] HUD tuân thủ **Cinematic Scene-Driven HUD (Option 4)**:
  - Cảnh Hook: Zero HUD, nội dung bắt đầu từ `y=160`.
  - Cảnh Deep-dive: Micro Breadcrumb + Step Pill màu Be Cát `#F3EBDD` tại `y=160`, nội dung bắt đầu từ `y=240`.
  - Cảnh Benchmark: Full Battle HUD cơ học tại `y=160..300`, nội dung bắt đầu từ `y=360`.
- [ ] Không sử dụng thanh Topbar cố định gò bó xuyên suốt video.
- [ ] Áp dụng đúng 1 trong **5 Ngữ Cảnh Nội Dung Cốt Lõi (Context Archetypes)**:
  - `product_tool_showcase`: Hero app window macOS dots, Keycombo trigger hoặc virtual cursor click CTA với ripple xanh mint.
  - `github_repo_deepdive`: Header repo chuẩn, Star Explosion bùng nổ, terminal typewriter và preview thật.
  - `architecture_theory`: Đường bus 8px, hạt xung dữ liệu thực thể (Tactile Data Packets) kích hoạt phản ứng nảy node.
  - `benchmark_fact_battle`: Split dual compare va chạm cơ học, counter quay tít hãm phanh, con dấu kiểm định.
  - `incident_post_mortem`: Dải alert đỏ, laser scanline hoặc micro-shake, terminal log khựng lại ở mã lỗi chí mạng.
- [ ] **Chuyển động tuân thủ Ma Trận Mục Đích Nhận Thức (Cognitive Purpose Motion Matrix)**: Animation được chọn đúng bản chất hành động kịch bản (Keycombo, Highlighter Sweep, Framing Brackets, Laser Scan, Bus Pulse, Stamp Slam).
- [ ] **Tuân thủ Strict Virtual Cursor Policy**: Trỏ chuột ảo xuất hiện không quá 1-2 lần/video và CHỈ dùng khi thể hiện tương tác web/app chân thực.
- [ ] Hard Quality Gate verified: Every deep-dive scene declares and contains at least 1 real visual asset in `assets/images/` (`brand_icon_tool` vector logos, OpenGraph / UI screenshots, dynamic SVG architecture diagrams, or code snippets).
- [ ] Continuous Motion Foundation: Snappy card reveal (280ms), continuous camera slow-drift (1.0 -> 1.025x), và dynamic pan/tilt.
- [ ] Bento cards use 2px/3.5px solid `#181826` borders and flat drop shadow `0 6px 0` hoặc `0 10px 0 #9D91E8`.
- [ ] All corporate logos and technical UI icons resolved via `brand_icon_tool` (no hand-drawn SVG logos).
- [ ] Typography uses `Inter` for bold headlines/labels and `IBM Plex Mono` for numbers/code.
- [ ] High-contrast readability: numbers ≥ 54px (hero 64–84px), labels ≥ 28px.
- [ ] Animations use GSAP with Snappy Developer Motion (`cubic-bezier(0.16, 1, 0.3, 1)` in 280ms).
- [ ] Subtitles and voiceover perfectly synchronized with on-screen visual beats.
- [ ] Render verified 1080×1920 without layout overlap, overflow, or render artifacts.
