---
name: coffat-media-director
description: Master Director Router & Channel Dispatcher for COFFAT MEDIA's 5 faceless vertical video channels (Mạch Số, Vạn Vật, Dấu Mốc, Tâm Trí, Bàn Cờ). Detects channel context from user prompts and routes execution to the dedicated channel director skill (mach-so-director, van-vat-director, dau-moc-director, tam-tri-director, ban-co-director).
---

# COFFAT MEDIA — Master Director Router & Channel Dispatcher

> **System Role**: Master Director Router & Dispatcher  
> **Channels Governed**: **Mạch Số**, **Vạn Vật**, **Dấu Mốc**, **Tâm Trí**, **Bàn Cờ**  
> **Architecture**: Modular Channel Skills (`*-director`) + Atelier Hand-Authoring (HyperFrames 9:16)  
> **Rule Zero Contract**: Mọi video sản xuất bắt buộc tuân thủ cỗ máy trạng thái CofVid (`research -> proposal -> script -> scene_plan -> assets -> edit -> compose`).

---

## 1. Cơ Chế Điều Phối Kênh Tự Động (Channel Dispatcher Engine)

Khi người dùng gửi yêu cầu sản xuất video, Agent phân tích ngữ cảnh, từ khóa và chủ đề để **tự động kích hoạt skill đạo diễn chuyên trách tương ứng**:

| Tên Kênh | Ký Hiệu | Từ Khóa Nhận Diện Trong Prompt | Skill Đạo Diễn Chuyên Trách Bắt Buộc Kích Hoạt |
|---|---|---|---|
| **Mạch Số** | `mach-so` | `mạch số`, `mach so`, `developer`, `code`, `thuật toán`, `kiến trúc hệ thống`, `github`, `ai tech`, `bento` | **`mach-so-director`** |
| **Vạn Vật** | `van-vat` | `vạn vật`, `van vat`, `khoa học`, `vũ trụ`, `tự nhiên`, `sinh học`, `động vật`, `vật lý`, `blueprint` | **`van-vat-director`** |
| **Dấu Mốc** | `dau-moc` | `dấu mốc`, `dau moc`, `lịch sử`, `chiến dịch`, `sự kiện`, `nhân vật lịch sử`, `tư liệu`, `vox collage` | **`dau-moc-director`** |
| **Tâm Trí** | `tam-tri` | `tâm trí`, `tam tri`, `tâm lý`, `hành vi`, `cảm xúc`, `triết học`, `nội tâm`, `chữa lành`, `thought typography` | **`tam-tri-director`** |
| **Bàn Cờ** | `ban-co` | `bàn cờ`, `ban co`, `kinh doanh`, `kinh tế`, `tập đoàn`, `tài chính`, `thương trường`, `chiến lược`, `bento kính mờ` | **`ban-co-director`** |

> ⚠️ **LƯU Ý QUAN TRỌNG CHO AGENT**: Sau khi xác định được kênh, Agent **BẮT BUỘC** mở và tuân thủ toàn diện hướng dẫn trong file `SKILL.md` của skill đạo diễn chuyên trách đó (`mach-so-director`, `van-vat-director`, v.v.). Không tự ý gộp chung hoặc làm mờ ranh giới phong cách giữa các kênh.

---

## 2. Ma Trận Bản Sắc 5 Kênh (Channel Identity Matrix)

| Kênh | Phong Cách Phê Duyệt | Nền & Canvas | Accent Màu Chính | Typography | Giọng VieNeu-TTS |
|---|---|---|---|---|---|
| **Mạch Số** | Neo-Brutalist Tactile Bento 2026 | Lavender (`#CBC3FA`) + dot-grid | `mint-green` (`#10B981`), `coral-red` (`#FF4757`) | `Inter` + `IBM Plex Mono` | `Hải Đăng` (1.05x, thông minh, rành mạch) |
| **Vạn Vật** | National Geographic Field Journal & Minimalist Blueprint | Warm Parchment (`#FAF6EE` / `#FAFAF7`) + viền kép | `botanical-teal` (`#397B72`), `mineral-blue` (`#83A7B4`) | `Source Serif 4` / `Lora` + `Inter` | `Mai Anh` (1.0x, kỳ vĩ, truyền cảm) |
| **Dấu Mốc** | Vox Paper Collage & Archival Documentary | Archival Paper (`#FAF8F3`) & Parchment (`#E8DFD0`) | `burgundy` (`#873F43`), `antique-gold` (`#B18B55`) | `Playfair Display` + `Inter` + `Mono` | `Hải Đăng` (1.0x, sử thi, hào hùng) |
| **Tâm Trí** | Humanist Editorial & Kinetic Thought Typography | Warm Paper (`#FAFAF7`) & Dusty Rose (`#E9DED8`) | `muted-plum` (`#795C76`), `terracotta` (`#C47C70`) | `Lora` (Italics) + `Inter` | `Mai Anh` (1.0x, thấu cảm, sâu lắng) |
| **Bàn Cờ** | Swiss Financial Bento Monolith | Warm Paper (`#FAFAF7`) + Frosted Glass (`blur 16px`) | `forest-green` (`#376B50`), `brass` (`#B18D55`) | `Source Serif 4` + `Inter` + `Mono` | `Hải Đăng` (1.05x, sắc sảo, đĩnh đạc) |

---

## 3. Các Tiêu Chuẩn Nền Tảng Chung (Universal Foundation Standards)

Bất kể sản xuất video cho kênh nào, tất cả các đạo diễn đều phải tuân thủ:

### A. Quy Chuẩn Khung Hình 9:16 & Safe Area
- **Độ phân giải chuẩn**: `1080 × 1920 px` (Tỷ lệ dọc 9:16).
- **Vùng an toàn (Universal Safe Area)**:
  - Lề trái & phải: Tối thiểu **64px** (Mạch Số, Bàn Cờ) đến **90px** (Vạn Vật, Dấu Mốc, Tâm Trí).
  - Lề trên: Tối thiểu **140px – 160px** (tránh bị che bởi avatar/thanh tìm kiếm TikTok/Reels).
  - Lề dưới: Tối thiểu **240px** (tránh bị che bởi caption/thanh tương tác người dùng).

### B. Triệt Tiêu Tuyệt Đối Giao Diện "Generic AI Slop"
- ❌ **CẤM KHỐI 3D TRÔI NỔI & TIA SÉT GLOWING**: Không khối lập phương 3D xoay, không bộ não phát sáng viễn tưởng, không gradient tím-cyan AI.
- ❌ **CẤM KHUÔN MẶT SÁP MIDJOURNEY**: Mọi khuôn mặt người trong video phải là tư liệu B-roll thật hoặc ảnh chụp báo chí/lịch sử có nguồn gốc kiểm chứng.
- ❌ **CẤM MOCKUP SVG NGUYỆCH NGOẠC**: Bắt buộc giải quyết qua `brand_icon_tool` để hiển thị logo chính hãng.

### C. Tri-Layer Audio Mix (Sound Design OS)
- **Layer 1 (Thoại chính - VieNeu-TTS Offline)**: `0 dB` tham chiếu (-14 LUFS). Giọng đọc offline chuẩn xác 100% không tốn chi phí API (`Hải Đăng` hoặc `Mai Anh`).
- **Layer 2 (Hiệu ứng xúc giác - Tactile SFX)**: `-10 dB` đến `-12 dB`. Đồng bộ chính xác với nhịp chuyển động GSAP timeline.
- **Layer 3 (Nền cảm xúc - Dynamic BGM)**: Tự động né giọng (ducking) xuống `-18 dB` khi có lời thoại, dâng lên `-12 dB` ở các khoảng lặng chuyển cảnh.

---

## 4. Hướng Dẫn Kích Hoạt Từng Bước Cho Agent

1. **Bước 1**: Nhận đề tài từ user. Xác định rõ kênh đích bằng Bảng Điều Phối ở Mục 1.
2. **Bước 2**: Kích hoạt skill đạo diễn chuyên trách:
   - Nếu là Mạch Số: Đọc `.agents/skills/mach-so-director/SKILL.md`
   - Nếu là Vạn Vật: Đọc `.agents/skills/van-vat-director/SKILL.md`
   - Nếu là Dấu Mốc: Đọc `.agents/skills/dau-moc-director/SKILL.md`
   - Nếu là Tâm Trí: Đọc `.agents/skills/tam-tri-director/SKILL.md`
   - Nếu là Bàn Cờ: Đọc `.agents/skills/ban-co-director/SKILL.md`
3. **Bước 3**: Khởi chạy cỗ máy trạng thái CofVid theo đúng SOP 7 bước được quy định trong skill chuyên trách đó.
4. **Bước 4**: Báo cáo tiến độ và dừng lại tại các Cổng Phê Duyệt Bắt Buộc (Proposal Gate & Scene Plan Gate).
