# AI AGENT WORKFLOW — ATELIER COMPOSITION IN HYPERFRAMES

> **Quy trình chi tiết dành cho AI Agent trong CofVid để sản xuất video tài liệu dọc 9:16 độc bản (Bespoke Atelier Production) dựa trên 5 file `design.md`.**

---

## 1. Vòng Đời Sản Xuất Atelier (Production Lifecycle)

```
[1. Tiếp Nhận Chủ Đề & Phân Loại Kênh]
   ├── Công nghệ, phần mềm, AI, internet      ──> Mạch Số (`mach-so`)
   ├── Vũ trụ, tự nhiên, sinh học, vật lý     ──> Vạn Vật (`van-vat`)
   ├── Lịch sử, đế chế, nhân vật, biến cố     ──> Dấu Mốc (`dau-moc`)
   ├── Tâm lý học, nhận thức, hành vi con người ──> Tâm Trí (`tam-tri`)
   └── Kinh doanh, kinh tế, thị trường, doanh nghiệp ──> Bàn Cờ (`ban-co`)
               │
               ▼
[2. Kịch Bản & Lồng Tiếng AI (VieNeu-TTS)]
   ├── Soạn kịch bản súc tích (45s – 60s), phân cảnh theo nhịp kể tài liệu
   └── Tạo âm thanh narration qua VieNeu-TTS (Hải Đăng hoặc Mai Anh)
               │
               ▼
[3. Thiết Kế Âm Thanh Ngữ Cảnh (Sound Design OS)]
   ├── Tham khảo gợi ý trong `vertical-video-brand-kit/<channel>/audio-manifest.json`
   ├── Chủ động chọn BGM phù hợp nhịp cảm xúc (kịch tính, lắng đọng, hay phân tích)
   └── Bố trí các điểm nổ SFX (`camera-shutter`, `click`, `whoosh`, `ding`) khớp visual
               │
               ▼
[4. Quy Trình Hand-Authoring 3 Bước Cho Từng Phân Cảnh]
   ├── BƯỚC 1: Đọc `design.md` của kênh, xác định Scene Pattern tương ứng
   │   (Question/Hook, Context, Mechanism, Evidence, Implication, Closing)
   ├── BƯỚC 2: Tự tay viết code HTML/CSS/GSAP bespoke cho cảnh
   │   - Nền warm-white `paper` (hoặc full-bleed footage)
   │   - Canh lề safe margin (L/R 90px, Top 140px, Bottom 300px)
   │   - Typography đúng font và tỷ lệ quy định
   │   - GSAP timeline animation đồng bộ chính xác với audio và SFX
   └── BƯỚC 3: Đối chiếu với Quality Checklist (Mục 14 hoặc 11 của `design.md`)
               │
               ▼
[5. Tổng Hợp Hyperframes & Render MP4]
   └── Ghép nối các phân cảnh vào composition và gọi `video_compose` xuất video 1080×1920
```

---

## 2. Hướng Dẫn Kỹ Thuật Viết Code Bespoke Cho Phân Cảnh

### A. Thiết Lập Khung Hình 1080 × 1920
Mọi cảnh quay đều có cấu trúc cơ bản tuân thủ vùng an toàn:
```html
<div class="scene-container" style="
  width: 1080px; 
  height: 1920px; 
  background-color: #FAFAF7; /* Paper warm-white */
  color: #222222; /* Ink */
  position: relative; 
  overflow: hidden;
  box-sizing: border-box;
">
  <!-- Safe Area Wrapper -->
  <div style="
    position: absolute; 
    top: 140px; 
    bottom: 300px; 
    left: 90px; 
    right: 90px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  ">
    <!-- Nội dung phân cảnh bespoke tại đây -->
  </div>
</div>
```

### B. Mẫu Quy Hoạch Typography
- **Mạch Số**: Dùng font `Inter` đậm cho tiêu đề (`font-size: 88–116px; line-height: 0.98`), `IBM Plex Mono` cho các nhãn kỹ thuật, thông số.
- **Dấu Mốc**: Dùng font có chân trang trọng `Playfair Display` cho câu mở đầu lịch sử (`font-size: 88–114px`), thân bài `Inter`.
- **Bàn Cờ**: Dùng font `Source Serif 4` / `Lora` cho tiêu đề bài toán kinh tế, `IBM Plex Mono` cho các con số tài chính có đơn vị tiền tệ rõ ràng.

### C. Quy Chuẩn Đạo Đức & Xác Thực Bắt Buộc
- **Dấu Mốc (History)**: Nếu cảnh quay sử dụng hình ảnh phục dựng bằng AI, Agent **BẮT BUỘC** phải đưa tem nhãn minh bạch vào góc trên khung hình:
  ```html
  <div class="archive-disclosure" style="
    font-family: 'IBM Plex Mono', monospace; 
    font-size: 20px; 
    color: #873F43; 
    border: 1px solid #873F43; 
    padding: 6px 14px;
    align-self: flex-start;
  ">[TÁI HIỆN MINH HỌA // AI RECONSTRUCTION]</div>
  ```
- **Bàn Cờ / Mạch Số / Vạn Vật**: Các con số, biểu đồ, cơ chế đều phải ghi rõ nguồn gốc (e.g., `SEC Form 10-K`, `Nature`, `ArXiv`, `NASA`).

---

## 3. Checklist Tự Kiểm Tra Trước Khi Render

Trước khi bàn giao video sang bước render của Hyperframes, Agent bắt buộc phải tự đối soát:
- [ ] Tỷ lệ canvas chuẩn 1080 × 1920 (9:16 dọc).
- [ ] Không có chữ quan trọng lọt ra ngoài safe margin (L/R 90px, Top 140px, Bottom 300px).
- [ ] Màu nền đồ họa là warm-white / paper (tránh nền đen neon phát sáng rẻ tiền).
- [ ] Mỗi khung hình chỉ truyền tải duy nhất một thông điệp hoặc cơ chế chính.
- [ ] Chuyển động GSAP tinh tế, không có hiệu ứng rung lắc (shake), bounce hoạt hình hay glitch tùy tiện.
- [ ] Phụ đề (Subtitles) tối đa 2 dòng, cỡ 44–54px, không che mặt nhân vật hoặc chi tiết tài liệu.
