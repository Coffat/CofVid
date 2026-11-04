---
name: dau-moc-director
description: Dedicated production director skill for COFFAT MEDIA's DẤU MỐC channel (History, civilization, historical battles, world-changing turning points). Governs the 7-stage CofVid pipeline in Atelier Mode using Vox Paper Collage & Archival Documentary standards.
---

# DẤU MỐC — Dedicated Production Director Skill (Atelier Hand-Authoring)

> **Channel Code**: `dau-moc` | **Audience**: History buffs, documentary lovers, geopolitical & civilization researchers  
> **Approved Aesthetic**: **Style 6 — Vox Paper Collage & Archival Documentary (Vox Approved 2026)**  
> **Primary Canvas**: Warm Archival Paper (`#FAF8F3`) & Antique Parchment (`#E8DFD0`) with torn-paper collage  
> **Narration Voice**: **VieNeu-TTS Hải Đăng** (Trang trọng, hào hùng, sử thi, đĩnh đạc, tốc độ 1.0x)  
> **Source of Truth**: `vertical-video-brand-kit/dau-moc/design.md`

---

## PHẦN 1: SỔ TAY ĐỘC LẬP TOÀN DIỆN (Self-Contained Deep Handbook)

### 1. Visual Thesis & Bản Sắc Kênh
- **Sứ mệnh**: Kể những câu chuyện lịch sử, nền văn minh, phát minh vĩ đại, nhân vật kiệt xuất, các cuộc xung đột và những bước ngoặt xoay chuyển vận mệnh thế giới.
- **Visual Thesis**: Lịch sử phải được cảm nhận như một **cuộc điều tra tư liệu thực thụ thông qua chứng cứ gốc hữu hình (primary sources)** — chứ không phải bộ phim phục trang Hollywood với bộ lọc màu rẻ tiền hay hình ảnh AI tái hiện giả tạo.
- **Ngôn ngữ chủ đạo**: Vox-style paper collage. Cắt dán tư liệu báo chí thời đại với mép giấy xé tự nhiên, ảnh đen trắng lưu trữ bảo tàng, bản đồ gốc với nét bút chì animated vẽ lộ trình chiến dịch, điểm xuyết vệt bút dạ quang burgundy (`#873F43`) và con dấu sáp niêm phong cổ kính (`#B18B55`).

### 2. Thông Số Kỹ Thuật (Design Tokens & Safe Area)
- **Kích thước khung hình**: `1080 × 1920 px` (Tỷ lệ dọc 9:16).
- **Vùng an toàn (Safe Area)**: Lề trái/phải **90px**, Lề trên **160px**, Lề dưới **240px**.
- **Bảng màu cốt lõi**:
  - Master Canvas: `paper` (`#FAF8F3`) và `parchment` (`#E8DFD0`) làm bề mặt giấy lưu trữ tài liệu.
  - Tấm nền tương phản: `white` (`#FFFFFF`) cho các mảnh báo masthead, `deep` (`#211D1B`) cho vignette góc tối.
  - Nét chữ & Đường kẻ: `ink` (`#292624`) cho nội dung báo chí, `muted-ink` (`#716B63`) cho nguồn trích dẫn và tọa độ lưu trữ.
  - Accent lịch sử: `burgundy` (`#873F43`) là màu đỏ rượu vang chủ đạo cho ngày tháng bước ngoặt và vệt bút dạ quang; `antique-gold` (`#B18B55`) cho tem niêm phong sáp, huy chương và hoa tiêu la bàn; `sepia-tint` (`#D4C4B5`) cho tấm đế ảnh cũ.
- **Hệ Typography**:
  - Tiêu đề & Tít báo Masthead: **Playfair Display** hoặc **Source Serif 4** (Serif cổ điển, uy nghi, gợi nhắc báo chí thế kỷ 19-20).
  - Nội dung thuyết minh & Trích dẫn: **Inter** (Dễ đọc, tương phản sắc nét trên nền giấy).
  - Niên đại, Mốc thời gian, Mã tài liệu: **IBM Plex Mono** (Định dạng ngày tháng chuẩn: `14.07.1789`, `DOC_ARCHIVE // 1945`).

### 3. Hệ Thống 5 Scene Archetypes (Ngũ Phân Hệ Tư Liệu Lịch Sử)
1. `newspaper_headline_flash`: Mảnh báo thời đại cắt dán lớp lang (newspaper collage), tít báo giật gân, vệt bút dạ quang burgundy tô đậm từ khóa bước ngoặt.
2. `cartographic_battle_route`: Bản đồ địa lý / hải trình cổ với nét bút chì animated vẽ mũi tên tiến quân hoặc lộ trình khám phá từng chặng.
3. `archival_photo_evidence`: Ảnh tư liệu đen trắng của nhân vật lịch sử hoặc bức thư tay giải mật được đặt trang trọng trong khung đế ảnh lưu trữ bảo tàng.
4. `geopolitical_chronology_split`: Trục thời gian đối chiếu nguyên nhân - hệ quả (cause and effect) hoặc so sánh chiến lược giữa 2 thế lực đối đầu.
5. `turning_point_verdict`: Thời khắc hiệp định được ký kết hoặc biến cố lịch sử ngã ngũ; con dấu sáp niêm phong đỏ dập xuống đóng lại một chương lịch sử.

### 4. Bộ 5 Evidence Props & Motion Toolkit (Chuẩn Vox)
1. **Continuous 2.5D Camera Drift**: Toàn bộ bố cục giấy duy trì chuyển động trôi chậm đa chiều (pan & micro-rotate $0.5^\circ$), tạo cảm giác camera đang lướt qua bàn làm việc của một sử gia.
2. **Paper Torn Cutouts & Tactile Shadows**: Các mảnh tư liệu cắt dán có đổ bóng êm (`0 8px 24px rgba(41, 38, 36, 0.12)`), mép cắt xé giấy có vân sần.
3. **Animated Pencil & Ink Route Lines**: Đường lộ trình chiến dịch vẽ dần bằng `strokeDashoffset` mô phỏng nét bút chì vẽ tay trên bản đồ cổ.
4. **Burgundy Translucent Highlighter Wash**: Vệt dạ quang burgundy (`rgba(135, 63, 67, 0.25)`) quét ngang dòng tít báo đúng lúc giọng đọc nhắc tới.
5. **Mandatory Reconstruction Labeling**: Mọi hình ảnh phục dựng minh họa hoặc bản đồ tái hiện bắt buộc mang tem chuẩn: `[TÁI HIỆN MINH HỌA // AI RECONSTRUCTION]`.

### 5. Bộ Rào Chắn Anti-AI Tuyệt Đối (Anti-Patterns)
- ❌ **CẤM KHUÔN MẶT AI MIDJOURNEY DA SÁP**: Tuyệt đối không vẽ mặt binh lính, danh nhân lịch sử bằng AI. Bắt buộc dùng ảnh chụp tư liệu thật, tranh khắc gỗ, hoặc tượng điêu khắc bảo tàng.
- ❌ **CẤM TÀI LIỆU LỊCH SỬ BỊA ĐẶT**: Không tự bịa tít báo hoặc nội dung hiệp ước; mọi trích dẫn phải có xuất xứ thực tế.
- ❌ **CẤM BỘ LỌC SEPIA Ố VÀNG BẨN THỈU**: Không phủ lớp màng màu vàng bẩn đè lên toàn video; nền giấy phải sáng sạch, trang trọng (`#FAF8F3`).

---

## PHẦN 2: QUY TRÌNH SOP 7 BƯỚC CHO DẤU MỐC (Step-by-Step Pipeline SOP)

### Bước 1: `research` (Xác minh Sử liệu & Mốc Thời Gian)
- Thu thập tài liệu lưu trữ gốc: Ngày/tháng/năm chính xác, tên chiến dịch, điều khoản hiệp ước, diễn biến các bên.
- Tìm kiếm tư liệu báo chí thời đại (The New York Times, Le Figaro, Nhân Dân, báo chí đương thời).
- Ghi nhận đầy đủ nguồn vào `grounded_facts.json`.

### Bước 2: `proposal` (Đề xuất & 7 Quyết định Bắt buộc)
- Tổng hợp và ghi nhận vào `decision_log.json`:
  1. `approval_policy`: Dừng phê duyệt tại cổng proposal & scene_plan.
  2. `music_source`: Track Orchestral Cinematic Trầm hùng / Tiếng đàn Cello lịch sử.
  3. `voice_selection`: **VieNeu-TTS Hải Đăng (1.0x)** (Hào hùng, đĩnh đạc, trang trọng).
  4. `playbook_selection`: Dấu Mốc Style 6 Vox Paper Collage & Archival.
  5. `composition_mode`: `atelier` (Hand-authoring).
  6. `render_runtime_selection`: `hyperframes`.
  7. `concept_selection`: Chọn 1 lát cắt lịch sử kịch tính nhất từ 3+ options.
- **Hard Gate**: Chờ user chấp thuận proposal.

### Bước 3: `script` (Kịch bản Voiceover Sử Thi)
- Giọng điệu: Hào hùng nhưng khách quan, kịch tính, lôi cuốn, tái hiện không khí thời đại.
- Cấu trúc: Sự kiện khởi đầu -> Diễn biến dồn dập -> Giây phút quyết định -> Hệ quả lâu dài.
- Độ dài: 140–155 từ cho video 60s.

### Bước 4: `scene_plan` (Kế hoạch Phân Cảnh Tư Liệu)
- Phân bổ 5–6 cảnh, gắn đúng 1 trong 5 Scene Archetypes cho từng cảnh.
- Ghi rõ nguồn ảnh lưu trữ và bản đồ cần sử dụng.
- Đánh dấu các mốc niên đại (Dates) cần highlight to rõ trên màn hình.
- **Hard Gate**: Dừng lượt chờ user phê duyệt scene_plan.

### Bước 5: `assets` (Thu thập Ảnh Tư Liệu & Bản Đồ Gốc)
- Tìm kiếm ảnh đen trắng lịch sử từ Wikimedia Commons, bảo tàng số, thư viện tư liệu quốc gia.
- Cắt ảnh thành dạng paper cutout (loại bỏ phông nền hoặc bo viền giấy trắng).
- Chuẩn bị tem `[TÁI HIỆN MINH HỌA // AI RECONSTRUCTION]` nếu có sơ đồ mô phỏng.
- Lưu toàn bộ vào `assets/images/`.

### Bước 6: `edit` (Xử lý Âm Thanh VieNeu-TTS Hải Đăng)
- Sinh giọng đọc `Hải Đăng` với âm lượng đĩnh đạc, nhịp điệu dứt khoát.
- Đồng bộ timestamp chính xác với từng sự kiện lịch sử trên màn hình.
- Mix âm thanh Tri-Layer: Voiceover (0 dB), SFX tiếng đánh máy chữ cơ, tiếng lật giấy báo, tiếng sáp dập (`-10 dB`), BGM dàn nhạc giao hưởng trầm trồ (`-18 dB`).

### Bước 7: `compose` (Atelier Hand-Authoring HyperFrames)
- Viết mã nguồn HyperFrames bespoke:
  - Bố cục cắt dán giấy Vox Style trên nền `#FAF8F3`.
  - Hiệu ứng nét bút chì vẽ lộ trình, vệt dạ quang burgundy.
  - GSAP camera drift chậm rãi, trang trọng.
- Thực hiện UI/UX Pro Max Audit (độ tương phản chữ, an toàn 9:16).
- Chạy `npx hyperframes render` xuất file MP4 1080×1920.
