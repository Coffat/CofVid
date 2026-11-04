# COFFAT MEDIA — 9:16 VERTICAL VIDEO DESIGN SPECIFICATIONS (ATELIER SYSTEM)

> **Hệ thống Design Specification chuẩn điện ảnh tài liệu dọc 9:16 (1080 × 1920) cho 5 kênh Faceless Documentary & Explainer của Coffat Media.**

---

## 1. Triết Lý Thiết Kế & Định Hướng Atelier

Hệ sinh thái Coffat Media vận hành theo cơ chế **Atelier Hand-Authoring**:
- **KHÔNG sử dụng HTML template dập khuôn cố định**: Thay vì các khung giao diện tĩnh với placeholder `{{variable}}` cứng nhắc, mỗi phân cảnh được AI Agent tự tay viết mã (hand-authored) HTML/CSS/GSAP độc bản cho từng nội dung cụ thể trong Hyperframes.
- **Nguồn chân lý duy nhất (Single Source of Truth)**: Mỗi kênh được định nghĩa toàn diện bởi một file `design.md` độc lập, quy định tỉ mỉ về phong cách thẩm mỹ, hệ thống màu sắc, thang typography, safe area, bố cục khung cảnh, nguyên lý chuyển động và các anti-patterns cần tránh.

---

## 2. Bản Đồ 5 Kênh & File `design.md`

| Kênh | Phong Cách Visual | Bảng Màu Nền & Accent | Typography Chủ Đạo | File Đặc Tả Chi Tiết |
|---|---|---|---|---|
| **Mạch Số** | Swiss Editorial × Technology Magazine × Data Journalism | Nền `paper` (`#FAFAF7`), accent `signal-blue` (`#3157A4`), `signal-orange` (`#E27B50`) | `Inter` / `Manrope` (Headline), `IBM Plex Mono` (Tech) | [`mach-so/design.md`](./mach-so/design.md) |
| **Vạn Vật** | Scientific Editorial × Natural History Museum × Minimalist Infographic | Nền `paper` (`#FAFAF7`), accent `botanical-teal` (`#397B72`), `mineral-blue` (`#83A7B4`) | `Source Serif 4` / `Lora` (Headline), `Inter` (Body) | [`van-vat/design.md`](./van-vat/design.md) |
| **Dấu Mốc** | Historical Editorial × Archive Newspaper × Contemporary Documentary | Nền `paper` (`#FAF8F3`), accent `burgundy` (`#873F43`), `antique-gold` (`#B18B55`) | `Playfair Display` / `Source Serif 4` (Headline), `Inter` (Body) | [`dau-moc/design.md`](./dau-moc/design.md) |
| **Tâm Trí** | Humanist Editorial × Psychology Magazine × Swiss Minimalism | Nền `paper` (`#FAFAF7`), accent `muted-plum` (`#795C76`), `terracotta` (`#C47C70`) | `Lora` / `Source Serif 4` (Headline), `Inter` (Body) | [`tam-tri/design.md`](./tam-tri/design.md) |
| **Bàn Cờ** | Financial Journalism × Swiss Editorial × Corporate Annual Report | Nền `paper` (`#FAFAF7`), accent `forest-green` (`#376B50`), `brass` (`#B18D55`) | `Source Serif 4` / `Lora` (Headline), `Inter` (Body) | [`ban-co/design.md`](./ban-co/design.md) |

---

## 3. Cấu Trúc Thư Mục Brand Kit

```
vertical-video-brand-kit/
├── README.md                          # Tài liệu tổng quan hệ thống (file này)
├── AGENT_WORKFLOW.md                  # Hướng dẫn chi tiết cho AI Agent sản xuất tự động
├── NETWORK_REVIEW.md                  # Ma trận đối soát 8 chiều & QA Scorecard
├── audio-listening-room.html          # Phòng nghe thử trực tiếp toàn bộ BGM & SFX 5 kênh
├── shared/
│   ├── safe-zone-universal.json       # Tọa độ vùng an toàn chuẩn hóa đa nền tảng
│   └── safe-zone-overlay.svg          # Lớp phủ SVG trực quan để kiểm thử bố cục
├── mach-so/
│   ├── design.md                      # Nguồn chân lý thiết kế của kênh Mạch Số
│   ├── audio-manifest.json            # Thư viện gợi ý BGM & SFX theo ngữ cảnh
│   ├── color-tokens.json              # Dữ liệu màu dạng token có cấu trúc
│   ├── typography.json                # Thang font & line-height
│   ├── safe-zones.json                # Vùng an toàn mobile
│   └── motion-tokens.json             # Easing & nguyên lý chuyển động
├── van-vat/                           # Tương tự cho Vạn Vật
├── dau-moc/                           # Tương tự cho Dấu Mốc
├── tam-tri/                           # Tương tự cho Tâm Trí
└── ban-co/                            # Tương tự cho Bàn Cờ
```

---

## 4. Chính Sách Thiết Kế Âm Thanh Ngữ Cảnh (Adaptive Sound OS)

- **Gợi ý linh hoạt, không áp đặt cứng nhắc**: File `audio-manifest.json` trong mỗi kênh là danh mục BGM & SFX đã được kiểm duyệt chất lượng cao (bản quyền mở CC-BY 4.0).
- **AI Agent chủ động lựa chọn theo ngữ cảnh (Contextual Intelligence)**:
  - Agent đọc diễn biến câu chuyện trong từng phân cảnh để chọn bài nhạc mang sắc thái phù hợp nhất (kịch tính, lắng đọng, hay giải mã khoa học).
  - Agent tự động rải các điểm nổ hiệu ứng xúc giác (Tactile SFX) khớp chính xác với từng khoảnh khắc hình ảnh (ảnh chụp tư liệu, chỉ số chứng khoán nhảy số, dòng lệnh terminal, hay giác ngộ tâm lý).
- **Chuẩn trộn âm 3 lớp (Tri-Layer Audio)**: Thoại (-14 LUFS) > SFX (-10 dB) > BGM (-18 dB né giọng / -12 dB chuyển cảnh).

---

## 5. Quy Chuẩn Kỹ Thuật Hyperframes

- **Khung hình**: `1080 × 1920 pixels` (9:16 Portrait).
- **Vùng an toàn (Conservative Safe Margin)**: Canh lề Trái/Phải `90px`, Đỉnh `140px`, Đáy `300px` để bảo đảm thông tin quan trọng không bị che khuất bởi giao diện của TikTok, YouTube Shorts, Reels.
- **Phụ đề (Subtitles)**: Cỡ chữ `44–54px`, tối đa 2 dòng, đặt ở vùng an toàn nửa dưới, tương phản cao, highlight có chọn lọc bằng accent của kênh.
- **Render Engine**: Tích hợp trực tiếp với engine Hyperframes của CofVid (`render_runtime="hyperframes"`).
