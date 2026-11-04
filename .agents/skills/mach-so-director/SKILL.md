---
name: mach-so-director
description: Dedicated production director skill for COFFAT MEDIA's MẠCH SỐ channel (High-tech, AI, algorithms, software architecture, developer motion). Governs the 7-stage CofVid pipeline in Atelier Mode using Neo-Brutalist Tactile Bento and 2026 Developer Motion Standard.
---

# MẠCH SỐ — Dedicated Production Director Skill (Atelier Hand-Authoring)

> **Channel Code**: `mach-so` | **Audience**: Developers, tech professionals, AI builders, system engineers  
> **Approved Aesthetic**: **Neo-Brutalist Tactile Bento / Developer Motion 2026**  
> **Primary Canvas**: Lavender (`#CBC3FA`) with 40px technical dot-grid  
> **Narration Voice**: **VieNeu-TTS Hải Đăng** (Rành mạch, thông minh, điềm tĩnh, tốc độ 1.05x)  
> **Source of Truth**: `vertical-video-brand-kit/mach-so/design.md`

---

## PHẦN 1: SỔ TAY ĐỘC LẬP TOÀN DIỆN (Self-Contained Deep Handbook)

### 1. Visual Thesis & Bản Sắc Kênh
- **Sứ mệnh**: Giải mã kiến trúc máy tính, trí tuệ nhân tạo, giải thuật phân tán, hạ tầng phần mềm và các công nghệ định hình thế giới số.
- **Visual Thesis**: Kiến trúc điện toán phức tạp không phải là một "khoảng không vũ trụ đen kịt vô định"; nó phải **hữu hình, có cấu trúc bento xúc giác, cơ học và sáng tỏ ngay lập tức**.
- **Ngôn ngữ chủ đạo**: Bento cards xúc giác viền đen 2px/3.5px (`#181826`), đổ bóng phẳng tím đặc trưng (`0 6px 0` / `0 10px 0 #9D91E8`), nền tím Lavender (`#CBC3FA`) với lưới dot-grid kỹ thuật, và giao diện **Cinematic Scene-Driven HUD (Option 4)**.

### 2. Thông Số Kỹ Thuật (Design Tokens & Safe Area)
- **Kích thước khung hình**: `1080 × 1920 px` (Tỷ lệ dọc 9:16).
- **Vùng an toàn (Safe Area)**: Lề trái/phải **64px**, Lề trên **160px**, Lề dưới **240px**.
- **Lưới Modular 8px**:
  - Full-width card: `952px` (left: `64px`)
  - 2-column bento card: `456px` (col 1: `64px`, col 2: `560px`, khoảng hở `32px`)
- **Bảng màu cốt lõi**:
  - Master Canvas: `bg-lavender` (`#CBC3FA`) + dot-grid kỹ thuật (`#ABA0EE`, 40px).
  - Thẻ & Bề mặt: `surface-white` (`#FFFFFF`), `surface-sand` (`#F3EBDD` cho HUD/Micro-breadcrumbs), `surface-dark` (`#181826`).
  - Viền & Đổ bóng: Viền `2px` hoặc `3.5px solid #181826`, bóng đổ `0 6px 0 #9D91E8` (hoặc `0 10px 0 #9D91E8`).
  - Accent chức năng: `mint-green` (`#10B981` / nền `#D1FAE5`) biểu thị tối ưu, cache hit, verified; `coral-red` (`#FF4757` / nền `#FFE1E4`) biểu thị lỗi, crash, bottleneck; `purple-accent` (`#7A6BE0`) cho tag monospace.
- **Hệ Typography**:
  - Headline, Bento Title, Pill Badges: **Inter** (Weight 700–900, tight letter-spacing `-0.02em`).
  - Mã nguồn, Latency, Token metrics: **IBM Plex Mono** (Weight 600–700).
  - Tỷ lệ: Hero numbers `96–128px`, Tiêu đề bento `48–56px`, Nhãn nội dung `34–40px`, Monospace tag `28–34px`.

### 3. Hệ Thống 5 Scene Archetypes (Ngũ Phân Hệ Ngữ Cảnh)
1. `product_tool_showcase`: Cửa sổ macOS dots (`● ● ●`), địa chỉ URL monospace, nút action CTA, 2 cột tính năng sát thủ với icon vector chính hãng từ `brand_icon_tool`.
2. `github_repo_deepdive`: Header repo GitHub Octocat chính hãng, badge License, Star Explosion bùng nổ (`scale: 1.7 -> 1.0`), cửa sổ terminal IDE gõ lệnh typewriter, và khung preview thật từ repo.
3. `architecture_theory`: Sơ đồ 3 tầng nối bằng đường bus đen 8px. Hạt xung dữ liệu thực thể (Data Packets) bắn dọc bus làm node nảy cơ học `1.05x`.
4. `benchmark_fact_battle`: Full Battle HUD tại `y=160..300`, so găng 2 cột (Cột Trái đỏ san hô lỗi đối đầu Cột Phải xanh mint tối ưu), đồng hồ Odometer quay tít phanh gấp `expo.out`, con dấu `✓ BENCHMARK VERIFIED` dập xuống `-3°`.
5. `incident_post_mortem`: Dải Alert Strip đỏ rực (`HTTP 502`, `KERNEL PANIC`), cửa sổ Crash Console hiển thị stack trace/dòng lỗi thật, thẻ đo lường thiệt hại, con dấu đỏ `✓ ROOT CAUSE VERIFIED`.

### 4. Bộ 6 Developer Interaction Primitives & Quy Tắc Trỏ Chuột
- **1. Keycombo HUD (`⌘K`, `Enter`, `Tab`, `Esc`)**: Phím cơ lún xuống cơ học (`y: +4px`, bóng thu về `0 1px 0`, viền chớp sáng `#10B981`) kích hoạt gọi lệnh/tool.
- **2. Highlighter Sweep & Line Spotlight**: Vệt dạ quang quét ngang theo giọng đọc + Selective Focus (dòng active scale 1.02x, xung quanh mờ 40%).
- **3. Framing Brackets / HUD Reticle**: 4 góc ngắm cơ khí ôm sát viền thẻ để khóa chặt tiêu điểm nhận thức.
- **4. Laser Scanline / Radar Sweep**: Dải laser quét dọc khối code/file/sơ đồ để phân tích, biên dịch, hoặc debug lỗi.
- **5. SVG Bus Pulse & Node Micro-Bounce**: Hạt xung dữ liệu bắn dọc bus 8px làm node đích nảy nhẹ `1.05x`.
- **6. Mechanical Stamp Slam & Odometer Counter**: Con dấu kiểm định đỏ/xanh dập rầm rộ (`back.out(2.2)`, `-3°`) và đồng hồ số quay tít phanh gấp `expo.out`.
- 🖱️ **Strict Virtual Cursor Policy**: Trỏ chuột ảo `#global-cursor` xuất hiện **tối đa 1-2 lần/video** và CHỈ dùng khi thể hiện tương tác người dùng thực tế trên app/web UI. Tuyệt đối KHÔNG dùng làm gậy chỉ bảng.
- 🧠 **Cognitive Purpose Selection**: Chọn animation dựa trên ĐÚNG BẢN CHẤT HÀNH ĐỘNG kịch bản, không ép buộc cấm lặp máy móc.

### 5. Bộ Rào Chắn Anti-AI Tuyệt Đối (Anti-Patterns)
- ❌ **CẤM NỀN TỐI / ĐEN GRAPHITE**: Tuyệt đối không dùng nền đen kịt `#111820` hay xám đen. Nền Mạch Số là Lavender `#CBC3FA` kèm dot-grid.
- ❌ **CẤM LOGO / BIỂU ĐỒ SVG TỰ VẼ NGUYỆCH NGOẠC**: Bắt buộc giải quyết qua `brand_icon_tool` để lấy vector mark chính thức.
- ❌ **CẤM KHỐI 3D TRÔI NỔI & HOLOGRAM VIỄN TƯỞNG**: Không khối lập phương 3D xoay, không hiệu ứng phát sáng cyan-magenta AI rẻ tiền.
- ❌ **CẤM ĐOẠN VĂN DÀI**: Không viết cả đoạn văn bản lên video. Tối đa 5 từ mỗi nhãn, ưu tiên số liệu to và typography nổi bật.

---

## PHẦN 2: QUY TRÌNH SOP 7 BƯỚC CHO MẠCH SỐ (Step-by-Step Pipeline SOP)

Khi sản xuất video Mạch Số, Agent phải tuân thủ nghiêm ngặt cỗ máy trạng thái CofVid:

### Bước 1: `research` (Nghiên cứu & Đối soát Dữ liệu Sống)
- **Bắt buộc**: Chạy `web_data_grounder` để lấy dữ liệu thực tế từ live web / GitHub repo (Stars, Forks, License, Release Date, Kiến trúc, Thông số Benchmark).
- Ghi nhận đầy đủ vào `grounded_facts.json`. Không bịa đặt thông số kỹ thuật.

### Bước 2: `proposal` (Đề xuất & 7 Quyết định Bắt buộc)
- Tổng hợp và ghi nhận vào `decision_log.json`:
  1. `approval_policy`: Dừng phê duyệt tại cổng proposal & scene_plan.
  2. `music_source`: Track Tech Synth / Electronic Minimalist từ music library.
  3. `voice_selection`: **VieNeu-TTS Hải Đăng (1.05x)**.
  4. `playbook_selection`: Mạch Số Neo-Brutalist Tactile Bento 2026.
  5. `composition_mode`: `atelier` (Hand-authoring).
  6. `render_runtime_selection`: `hyperframes`.
  7. `concept_selection`: Lựa chọn 1 góc nhìn kỹ thuật đắt giá nhất từ 3+ options.
- **Hard Gate**: Dừng lượt và chờ user chấp thuận proposal.

### Bước 3: `script` (Kịch bản Voiceover Kỹ thuật)
- Nhịp điệu: Nhanh, rành mạch, điềm tĩnh, đầy tính thuyết phục kỹ thuật.
- Cấu trúc: Hook 3s đầu không HUD -> Đặt vấn đề/Nghẽn cổ chai -> Phân tích sâu kiến trúc -> Benchmark so sánh -> Bài học/Kết luận đanh thép.
- Độ dài: 140–160 từ cho video 60s (tốc độ đọc 2.5–2.8 từ/giây).

### Bước 4: `scene_plan` (Kế hoạch Phân Cảnh & Visual Assets Mandate)
- Phân bổ 5–7 cảnh, gắn thẻ đúng 1 trong 5 Scene Archetypes cho từng cảnh.
- **Visual Assets Mandate (Hard Gate)**: Mọi cảnh deep-dive bắt buộc khai báo ít nhất 1 asset thật (`brand_icon_tool` corporate vector marks, OpenGraph preview, UI screenshot, code snippet).
- Áp dụng **Cognitive Purpose Motion Matrix**: Xác định trước animation primitive cho từng cảnh (Keycombo, Highlighter, Brackets, Laser, Bus Pulse, Stamp).
- Kiểm soát trỏ chuột ảo: Tổng số lần xuất hiện $\le 1-2$ lần.
- **Hard Gate**: Dừng lượt chờ user phê duyệt scene_plan.

### Bước 5: `assets` (Sourcing Tài Nguyên Thực Tế)
- Gọi `brand_icon_tool` để tải các logo công nghệ chính hãng (`github`, `docker`, `python`, `kubernetes`, `aws`, v.v.) thành file SVG/PNG vào `assets/images/`.
- Tạo code snippets định dạng monospace sạch, ảnh chụp kiến trúc/sự cố thật.
- Kiểm tra `assets/images/`: Tuyệt đối không để cảnh deep-dive dùng hộp rỗng.

### Bước 6: `edit` (Xử lý Âm Thanh VieNeu-TTS)
- Sinh giọng đọc `Hải Đăng` qua `vieneu_tts` với tốc độ 1.05x.
- Xuất word-level timestamps để đồng bộ khớp chính xác từng giây với chuyển động GSAP.
- Mix âm thanh Tri-Layer: Voiceover (0 dB tham chiếu), SFX cơ học tactile click/stamp/whoosh (`-10 dB`), BGM tech synth (`-18 dB` khi có thoại, `-12 dB` khi chuyển cảnh).

### Bước 7: `compose` (Atelier Hand-Authoring HyperFrames)
- Viết mã nguồn HyperFrames HTML/CSS/GSAP bespoke cho từng cảnh:
  - Nền Lavender `#CBC3FA` với dot-grid.
  - Bento cards viền đen 2px/3.5px, bóng tím `0 6px 0 #9D91E8`.
  - GSAP timeline khớp chuẩn xác thời lượng audio của VieNeu-TTS.
  - Sử dụng 6 Developer Interaction Primitives.
- Tiến hành UI/UX Pro Max Audit (WCAG 4.5:1, nhịp modular 8px, easing `cubic-bezier(0.16, 1, 0.3, 1)`).
- Chạy `npx hyperframes render` xuất file MP4 chất lượng cao 1080×1920.
