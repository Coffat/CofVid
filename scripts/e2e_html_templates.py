"""HTML Composition Generators for CofVid E2E Pipeline Testing.

Generates pixel-perfect, design.md-compliant HyperFrames HTML files for:
1. Mạch Số (Neo-Brutalist Tactile Bento)
2. Vạn Vật (Minimalist Blueprint / Scientific Diagram)
3. Dấu Mốc (Vox Paper Collage & Archival Documentary)
4. Tâm Trí (Kinetic Thought Typography)
5. Bàn Cờ (Bento Grid Financial Motion)
"""

from __future__ import annotations

def get_html_mach_so(duration: float = 16.0) -> str:
    return f"""<!doctype html>
<html lang="vi" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>MẠCH SỐ — Cảnh Báo Gartner 3.5T USD Hạ Tầng AI</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@600;700;800&family=Inter:wght@600;700;800;900&display=swap" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      :root{{--bg-lavender:#CBC3FA;--shadow-purple:#9D91E8;--surface-white:#FFFFFF;--surface-dark:#181826;--mint-green:#10B981;--mint-surface:#D1FAE5;--coral-red:#FF4757;--coral-surface:#FFE1E4;--font-sans:"Inter",sans-serif;--font-mono:"IBM Plex Mono",monospace;}}
      *{{margin:0;padding:0;box-sizing:border-box}}
      html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--bg-lavender);color:var(--surface-dark);font-family:var(--font-sans);-webkit-font-smoothing:antialiased}}
      #root{{position:relative;width:1080px;height:1920px;overflow:hidden}}
      .canvas-bg{{position:absolute;inset:0;background:#CBC3FA;z-index:0;overflow:hidden;pointer-events:none}}
      .dot-grid{{position:absolute;inset:0;background-image:radial-gradient(#ABA0EE 2.2px,transparent 2.2px);background-size:40px 40px;opacity:.45}}
      .top-banner-pill{{position:absolute;top:160px;left:64px;width:952px;height:88px;background:var(--surface-dark);border-radius:24px;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 0 var(--shadow-purple);z-index:120;overflow:hidden}}
      .bw{{font-size:38px;font-weight:900;letter-spacing:.01em;text-transform:uppercase;color:#FFF}}
      .bw.green{{color:var(--mint-green)}} .bw.red{{color:var(--coral-red)}}
      .inventory-bar{{position:absolute;top:272px;left:64px;height:72px;background:var(--surface-dark);border-radius:999px;padding:0 24px;display:flex;align-items:center;gap:12px;box-shadow:0 6px 0 var(--shadow-purple);z-index:125}}
      .inv-slot{{width:38px;height:38px;border-radius:10px;border:2.5px dashed rgba(255,255,255,.45);display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:900;color:#FFF}}
      .inv-slot.active{{background:var(--mint-green);border-color:var(--mint-green);color:#181826}}
      .inv-count{{font-size:32px;font-weight:900;color:#FFF;margin-left:8px;font-family:var(--font-mono)}}
      .latency-pill{{position:absolute;top:272px;right:64px;width:248px;height:72px;background:var(--mint-green);color:#FFF;border-radius:999px;box-shadow:0 6px 0 var(--shadow-purple);z-index:130;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:900;font-family:var(--font-mono)}}
      .card{{position:absolute;background:#FFF;border:3.5px solid var(--surface-dark);border-radius:32px;box-shadow:0 10px 0 var(--shadow-purple);color:var(--surface-dark);padding:36px;display:flex;flex-direction:column;justify-content:center;opacity:0}}
      .card.dark{{background:var(--surface-dark);color:#FFF}}
      .card.coral{{background:var(--coral-surface)}}
      .card.mint{{background:var(--mint-surface)}}
      .mono{{font-family:var(--font-mono);font-weight:700}}
      .num{{font-size:108px;font-weight:900;line-height:1;letter-spacing:-.03em}}
      .lbl{{font-size:38px;font-weight:800;line-height:1.2}}
      .pill-cta{{display:inline-flex;align-items:center;justify-content:center;border-radius:999px;font-weight:900;font-size:40px;background:var(--surface-dark);color:#FFF;border:3.5px solid var(--surface-dark);box-shadow:0 8px 0 var(--shadow-purple);height:100px;width:100%}}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-fps="30" data-duration="{duration}">
      <audio id="master-audio" src="assets/audio/final_mix.mp3" data-start="0" data-duration="{duration}" data-track-index="10" data-volume="1"></audio>
      <div class="canvas-bg"><div class="dot-grid"></div></div>
      <div class="top-banner-pill"><span class="bw green" id="banner-txt">CẢNH BÁO // GARTNER</span></div>
      <div class="inventory-bar">
        <div class="inv-slot" id="slot-1">1</div>
        <div class="inv-slot" id="slot-2">2</div>
        <div class="inv-slot" id="slot-3">3</div>
        <div class="inv-count" id="slot-count">0/3</div>
      </div>
      <div class="latency-pill" id="latency-box">12 ms</div>

      <!-- Scene 1: Stat Hero -->
      <div class="card dark" id="sc1-hero" style="left:64px;top:432px;width:952px;height:720px;align-items:center;text-align:center;">
        <div class="mono" style="color:var(--mint-green);font-size:32px;letter-spacing:0.1em;margin-bottom:16px;">HẠ TẦNG TOÀN CẦU</div>
        <div class="num" style="color:var(--mint-green);font-size:144px;">$3.5T</div>
        <div class="lbl" style="font-size:48px;margin-top:20px;max-width:800px;">Gartner Cảnh Báo: 3.5 Nghìn Tỷ USD Đổ Vào AI</div>
        <div class="mono" style="margin-top:32px;font-size:28px;opacity:0.7;">BÁO CÁO Q4/2026 // CAPEX DEFICIT</div>
      </div>

      <!-- Scene 2: Power Grid Paradox -->
      <div class="card coral" id="sc2-box1" style="left:64px;top:432px;width:952px;height:480px;">
        <div class="mono" style="color:var(--coral-red);font-size:32px;">NGHỊCH LÝ ĐIỆN NĂNG</div>
        <div class="num" style="color:var(--coral-red);font-size:116px;margin:16px 0;">85%</div>
        <div class="lbl">Trung tâm dữ liệu AI mới sẽ thiếu điện trước 2027.</div>
      </div>
      <div class="card" id="sc2-box2" style="left:64px;top:952px;width:952px;height:380px;">
        <div class="mono" style="color:var(--surface-dark);font-size:28px;">LƯỚI ĐIỆN QUÁ TẢI // CÔNG SUẤT 160 TWh</div>
        <div class="lbl" style="margin-top:16px;font-size:36px;">Áp lực tải lưới điện vượt ngưỡng cung ứng của toàn bộ Bắc Mỹ và Tây Âu gộp lại.</div>
      </div>

      <!-- Scene 3: Conclusion & CTA -->
      <div class="card dark" id="sc3-box1" style="left:64px;top:432px;width:952px;height:560px;align-items:center;text-align:center;">
        <div class="mono" style="color:var(--coral-red);font-size:32px;">BÀI TOÁN KINH TẾ // NGUY CƠ</div>
        <div class="num" style="color:var(--coral-red);font-size:96px;margin:16px 0;">ROI ÂM</div>
        <div class="lbl" style="font-size:44px;line-height:1.3;">Chi phí năng lượng vượt cả doanh thu mô hình.<br/>Lợi nhuận AI chính thức vỡ trận.</div>
      </div>
      <div id="sc3-cta" style="position:absolute;left:64px;top:1032px;width:952px;opacity:0;">
        <div class="pill-cta">+ THEO DÕI MẠCH SỐ</div>
      </div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;

      // S1 (0-5s)
      tl.to("#sc1-hero", {{ opacity: 1, y: 0, duration: 0.5, ease: "back.out(1.8)" }}, 0.3);
      tl.to("#slot-1", {{ className: "inv-slot active", duration: 0.1 }}, 0.8);
      tl.to("#slot-count", {{ textContent: "1/3", duration: 0.1 }}, 0.8);
      tl.to("#sc1-hero", {{ opacity: 0, duration: 0.3 }}, 4.8);

      // S2 (5-11s)
      tl.to("#banner-txt", {{ textContent: "NGHỊCH LÝ // THIẾU ĐIỆN", color: "#FF4757", duration: 0.1 }}, 5.0);
      tl.to("#latency-box", {{ backgroundColor: "#FF4757", textContent: "480 ms", duration: 0.2 }}, 5.0);
      tl.to("#sc2-box1", {{ opacity: 1, duration: 0.4, ease: "back.out(1.6)" }}, 5.2);
      tl.to("#sc2-box2", {{ opacity: 1, duration: 0.4, ease: "back.out(1.6)" }}, 5.6);
      tl.to("#slot-2", {{ className: "inv-slot active", duration: 0.1 }}, 6.2);
      tl.to("#slot-count", {{ textContent: "2/3", duration: 0.1 }}, 6.2);
      tl.to(["#sc2-box1", "#sc2-box2"], {{ opacity: 0, duration: 0.3 }}, 10.8);

      // S3 (11-16s)
      tl.to("#banner-txt", {{ textContent: "KẾT LUẬN // ROI ÂM", color: "#10B981", duration: 0.1 }}, 11.0);
      tl.to("#latency-box", {{ backgroundColor: "#10B981", textContent: "16 ms", duration: 0.2 }}, 11.0);
      tl.to("#sc3-box1", {{ opacity: 1, duration: 0.5, ease: "back.out(1.8)" }}, 11.2);
      tl.to("#sc3-cta", {{ opacity: 1, y: -10, duration: 0.4, ease: "power2.out" }}, 12.0);
      tl.to("#slot-3", {{ className: "inv-slot active", duration: 0.1 }}, 12.2);
      tl.to("#slot-count", {{ textContent: "3/3", duration: 0.1 }}, 12.2);
    </script>
  </body>
</html>"""


def get_html_van_vat(duration: float = 19.0) -> str:
    return f"""<!doctype html>
<html lang="vi" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>VẠN VẬT — Kính Thiên Văn IceCube Nam Cực</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      :root{{--paper:#FAFAF7;--white:#FFFFFF;--ink:#1C2526;--muted-ink:#667A78;--teal:#397B72;--teal-tint:rgba(57,123,114,0.12);--blue:#83A7B4;--rule:#E6E5DF;--font-sans:"Inter",sans-serif;--font-mono:"IBM Plex Mono",monospace;}}
      *{{margin:0;padding:0;box-sizing:border-box}}
      html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--paper);color:var(--ink);font-family:var(--font-sans);-webkit-font-smoothing:antialiased}}
      #root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--paper)}}
      .blueprint-grid{{position:absolute;inset:0;background-image:linear-gradient(to right,rgba(230,229,223,0.7) 1px,transparent 1px),linear-gradient(to bottom,rgba(230,229,223,0.7) 1px,transparent 1px);background-size:60px 60px;pointer-events:none}}
      .sci-header{{position:absolute;top:140px;left:64px;width:952px;height:84px;border-bottom:2px solid var(--ink);display:flex;align-items:center;justify-content:space-between;font-family:var(--font-mono);font-size:26px;font-weight:600;letter-spacing:0.04em}}
      .card{{position:absolute;background:var(--white);border:1.5px solid var(--rule);border-radius:24px;box-shadow:0 8px 24px rgba(28,37,38,0.06);padding:40px;opacity:0}}
      .mono{{font-family:var(--font-mono)}}
      .num{{font-size:112px;font-weight:800;letter-spacing:-0.03em;color:var(--teal)}}
      .lbl{{font-size:40px;font-weight:700;line-height:1.25}}
      .scale-bar{{display:flex;align-items:center;gap:12px;font-family:var(--font-mono);font-size:24px;color:var(--muted-ink);margin-top:20px}}
      .scale-line{{width:200px;height:4px;background:var(--ink);position:relative}}
      .scale-line::before,.scale-line::after{{content:"";position:absolute;top:-6px;width:2px;height:16px;background:var(--ink)}}
      .scale-line::before{{left:0}} .scale-line::after{{right:0}}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-fps="30" data-duration="{duration}">
      <audio id="master-audio" src="assets/audio/final_mix.mp3" data-start="0" data-duration="{duration}" data-track-index="10" data-volume="1"></audio>
      <div class="blueprint-grid"></div>
      <div class="sci-header">
        <span>VẠN VẬT // VẬT LÝ THIÊN VĂN</span>
        <span style="color:var(--teal)">ICECUBE OBSERVATORY · 89.99° S</span>
      </div>

      <!-- Scene 1: Depth Blueprint -->
      <div class="card" id="sc1-card" style="left:64px;top:380px;width:952px;height:780px;">
        <div class="mono" style="color:var(--teal);font-size:28px;margin-bottom:12px;">ĐỊA ĐIỂM // BĂNG VĨNH CỬU NAM CỰC</div>
        <div class="num">-2,500m</div>
        <div class="lbl" style="margin-top:16px;">Cỗ Máy Săn Hạt Dưới Đáy Băng Địa Cực</div>
        <p style="font-size:32px;color:var(--muted-ink);line-height:1.4;margin-top:24px;">IceCube sử dụng một kilomet khối băng tinh khiết ở độ sâu 2,500m làm môi trường tán xạ hạt tự nhiên lớn nhất hành tinh.</p>
        <div class="scale-bar">
          <div class="scale-line"></div>
          <span>THƯỚC ĐO: 500 MÉT</span>
        </div>
      </div>

      <!-- Scene 2: 100 TeV Detection -->
      <div class="card" id="sc2-card" style="left:64px;top:380px;width:952px;height:820px;background:var(--teal-tint);border-color:var(--teal);">
        <div class="mono" style="color:var(--teal);font-size:28px;">GHI NHẬN HẠT NĂNG LƯỢNG CAO</div>
        <div class="num" style="margin:20px 0;">100 TeV</div>
        <div class="lbl">Hạt Neutrino Năng Lượng 100 Tera-Electron-Volt</div>
        <p style="font-size:32px;color:var(--ink);line-height:1.4;margin-top:24px;">Mạng lưới 5,160 cảm biến quang học bắt trọn vết tích của hạt hạ nguyên tử bay xuyên thẳng qua lõi Trái Đất mà không bị cản trở.</p>
        <div class="mono" style="margin-top:36px;padding:20px;background:rgba(255,255,255,0.8);border-radius:12px;font-size:28px;">DOM ARRAY: 86 STRINGS // ACTIVE DETECTION</div>
      </div>

      <!-- Scene 3: Cherenkov Landing -->
      <div class="card" id="sc3-card" style="left:64px;top:380px;width:952px;height:840px;">
        <div class="mono" style="color:var(--teal);font-size:28px;">BỨC XẠ CHERENKOV // KHÁM PHÁ</div>
        <div class="lbl" style="font-size:52px;margin:28px 0;color:var(--teal);">Ánh Sáng Xanh Cherenkov Lóe Lên Trong Đáy Băng</div>
        <p style="font-size:36px;color:var(--ink);line-height:1.45;">Khi neutrino tương tác tạo muon siêu tốc, nó phát ra bức xạ Cherenkov — mở toang cánh cửa quang phổ nhìn thẳng vào các hố đen và siêu tân tinh xa xôi.</p>
        <div style="margin-top:40px;border-top:2px solid var(--rule);padding-top:24px;" class="mono">
          <span style="font-weight:700;color:var(--teal);">+ ĐĂNG KÝ THEO DÕI VẠN VẬT</span>
        </div>
      </div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;

      // S1 (0-6s)
      tl.to("#sc1-card", {{ opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }}, 0.3);
      tl.to("#sc1-card", {{ opacity: 0, duration: 0.4 }}, 5.6);

      // S2 (6-12s)
      tl.to("#sc2-card", {{ opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }}, 6.0);
      tl.to("#sc2-card", {{ opacity: 0, duration: 0.4 }}, 11.6);

      // S3 (12-19s)
      tl.to("#sc3-card", {{ opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }}, 12.0);
    </script>
  </body>
</html>"""


def get_html_dau_moc(duration: float = 17.0) -> str:
    return f"""<!doctype html>
<html lang="vi" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>DẤU MỐC — 13 Ngày Khủng Hoảng Tên Lửa Cuba 1962</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;700&family=Inter:wght@400;600;700&family=Playfair+Display:wght@700;900&display=swap" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      :root{{--paper:#FAF8F3;--parchment:#E8DFD0;--ink:#2B2420;--burgundy:#873F43;--gold:#B18B55;--rule:#DED8CF;--font-serif:"Playfair Display",serif;--font-sans:"Inter",sans-serif;--font-mono:"IBM Plex Mono",monospace;}}
      *{{margin:0;padding:0;box-sizing:border-box}}
      html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--paper);color:var(--ink);font-family:var(--font-sans);-webkit-font-smoothing:antialiased}}
      #root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--paper)}}
      .archival-header{{position:absolute;top:130px;left:64px;width:952px;height:90px;border-bottom:3px solid var(--burgundy);display:flex;align-items:center;justify-content:space-between;font-family:var(--font-mono);font-size:26px;font-weight:700;color:var(--burgundy)}}
      .card{{position:absolute;background:var(--paper);border:2px solid var(--rule);border-radius:16px;box-shadow:0 12px 32px rgba(43,36,32,0.1);padding:44px;opacity:0}}
      .highlight{{background:rgba(135,63,67,0.22);padding:0 8px;border-radius:4px}}
      .stamp{{border:4px solid var(--gold);color:var(--gold);padding:8px 24px;font-family:var(--font-mono);font-weight:700;font-size:28px;text-transform:uppercase;display:inline-block;border-radius:8px;transform:rotate(-2deg)}}
      .mono{{font-family:var(--font-mono)}}
      .serif{{font-family:var(--font-serif)}}
      .num{{font-size:120px;font-weight:900;color:var(--burgundy);line-height:1;margin:16px 0}}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-fps="30" data-duration="{duration}">
      <audio id="master-audio" src="assets/audio/final_mix.mp3" data-start="0" data-duration="{duration}" data-track-index="10" data-volume="1"></audio>
      <div class="archival-header">
        <span>[DẤU MỐC // HỒ SƠ LỊCH SỬ]</span>
        <span>CIA TOP SECRET // 1962</span>
      </div>

      <!-- Scene 1: U-2 Discovery -->
      <div class="card" id="sc1-card" style="left:64px;top:380px;width:952px;height:760px;background:var(--parchment);">
        <div class="stamp">GIẢI MẬT QUỐC GIA</div>
        <div class="mono" style="font-size:32px;margin-top:24px;color:var(--burgundy);font-weight:700;">14 THÁNG 10, 1962</div>
        <div class="serif" style="font-size:54px;font-weight:900;line-height:1.2;margin:20px 0;">Chuyến Bay Do Thám U-2 Thay Đổi Cả Lịch Sử</div>
        <p style="font-size:34px;line-height:1.4;color:var(--ink);">Bức ảnh chụp từ độ cao 21,000m làm rúng động Lầu Năm Góc: Liên Xô đang bí mật lắp đặt căn cứ tên lửa hạt nhân tầm trung tại Cuba.</p>
      </div>

      <!-- Scene 2: San Cristóbal Map -->
      <div class="card" id="sc2-card" style="left:64px;top:380px;width:952px;height:820px;">
        <div class="mono" style="color:var(--burgundy);font-size:28px;">TỌA ĐỘ SAN CRISTÓBAL // BÁN KÍNH TẤN CÔNG</div>
        <div class="num">140 KM</div>
        <div class="serif" style="font-size:46px;font-weight:700;line-height:1.2;">Chỉ Cách Bờ Biển Nước Mỹ 140 Cây Số</div>
        <p style="font-size:34px;line-height:1.45;margin-top:20px;">Tên lửa đạn đạo SS-4 với đầu đạn hạt nhân có thể vươn tới thủ đô Washington D.C. chỉ sau <span class="highlight">12 phút bay</span>.</p>
        <div class="mono" style="margin-top:32px;font-size:26px;color:var(--burgundy);border-left:4px solid var(--burgundy);padding-left:16px;">TÌNH TRẠNG BÁO ĐỘNG DEFCON 2 KÍCH HOẠT</div>
      </div>

      <!-- Scene 3: 13 Days Countdown -->
      <div class="card" id="sc3-card" style="left:64px;top:380px;width:952px;height:820px;background:var(--parchment);">
        <div class="stamp" style="border-color:var(--burgundy);color:var(--burgundy);">ĐỈNH ĐIỂM CHIẾN TRANH LẠNH</div>
        <div class="num" style="margin-top:24px;">13 NGÀY</div>
        <div class="serif" style="font-size:50px;font-weight:900;line-height:1.2;">Mười Ba Ngày Nghẹt Thở Của Nhân Loại</div>
        <p style="font-size:34px;line-height:1.45;margin-top:20px;">Nơi chỉ một nút bấm sai lầm có thể châm ngòi cuộc chiến tranh hạt nhân hủy diệt toàn cầu.</p>
        <div class="mono" style="margin-top:40px;font-size:28px;font-weight:700;color:var(--burgundy);">+ THEO DÕI DẤU MỐC LỊCH SỬ</div>
      </div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;

      // S1 (0-5.5s)
      tl.to("#sc1-card", {{ opacity: 1, duration: 0.5, ease: "power2.out" }}, 0.3);
      tl.to("#sc1-card", {{ opacity: 0, duration: 0.3 }}, 5.1);

      // S2 (5.5-11.5s)
      tl.to("#sc2-card", {{ opacity: 1, duration: 0.5, ease: "power2.out" }}, 5.5);
      tl.to("#sc2-card", {{ opacity: 0, duration: 0.3 }}, 11.1);

      // S3 (11.5-17s)
      tl.to("#sc3-card", {{ opacity: 1, duration: 0.5, ease: "power2.out" }}, 11.5);
    </script>
  </body>
</html>"""


def get_html_tam_tri(duration: float = 18.0) -> str:
    return f"""<!doctype html>
<html lang="vi" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>TÂM TRÍ — Hiện Tượng Deference To AI</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,500;0,600;1,500&display=swap" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      :root{{--paper:#FAFAF7;--ink:#231F20;--plum:#795C76;--terracotta:#C47C70;--dusty-rose:#E9DED8;--rule:#E7E2DF;--font-serif:"Lora",serif;--font-sans:"Inter",sans-serif;--font-mono:"IBM Plex Mono",monospace;}}
      *{{margin:0;padding:0;box-sizing:border-box}}
      html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--paper);color:var(--ink);font-family:var(--font-sans);-webkit-font-smoothing:antialiased}}
      #root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--paper)}}
      .essay-header{{position:absolute;top:140px;left:64px;width:952px;height:84px;border-bottom:1.5px solid var(--rule);display:flex;align-items:center;justify-content:space-between;font-family:var(--font-mono);font-size:26px;color:var(--plum)}}
      .card{{position:absolute;background:#FFF;border:1.5px solid var(--rule);border-radius:28px;box-shadow:0 12px 36px rgba(121,92,118,0.08);padding:48px;opacity:0}}
      .mono{{font-family:var(--font-mono)}}
      .serif{{font-family:var(--font-serif)}}
      .lbl{{font-size:52px;line-height:1.3;font-weight:600}}
      .terracotta{{color:var(--terracotta)}}
      .plum{{color:var(--plum)}}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-fps="30" data-duration="{duration}">
      <audio id="master-audio" src="assets/audio/final_mix.mp3" data-start="0" data-duration="{duration}" data-track-index="10" data-volume="1"></audio>
      <div class="essay-header">
        <span>TÂM TRÍ // TÂM LÝ HỌC NHẬN THỨC</span>
        <span>ESSAY NO. 4</span>
      </div>

      <!-- Scene 1: The Question -->
      <div class="card" id="sc1-card" style="left:64px;top:400px;width:952px;height:720px;">
        <div class="mono plum" style="font-size:28px;margin-bottom:24px;">SUY NGẪM // QUAN SÁT HÀNH VI</div>
        <div class="serif lbl">Bạn có nhận ra, chúng ta đang dần <span class="terracotta">ngừng đặt câu hỏi</span> trước mỗi câu trả lời của AI?</div>
        <p style="font-size:34px;color:#666;line-height:1.5;margin-top:32px;">Một sự chuyển dịch âm thầm trong thói quen tư duy hàng ngày của hàng trăm triệu người dùng trên toàn thế giới.</p>
      </div>

      <!-- Scene 2: Cognitive Deference -->
      <div class="card" id="sc2-card" style="left:64px;top:400px;width:952px;height:780px;background:var(--dusty-rose);">
        <div class="mono plum" style="font-size:28px;">HIỆN TƯỢNG TÂM LÝ HỌC</div>
        <div class="serif lbl" style="margin:20px 0;font-size:56px;">Deference to AI</div>
        <div class="mono terracotta" style="font-size:34px;font-weight:700;">NHƯỢNG BỘ THUẬT TOÁN</div>
        <p style="font-size:34px;color:var(--ink);line-height:1.5;margin-top:24px;">Khi bộ não con người tự động tắt cơ chế phản biện logic, nhường toàn quyền thẩm định chân lý cho dòng chữ trên màn hình.</p>
      </div>

      <!-- Scene 3: Conclusion & Warning -->
      <div class="card" id="sc3-card" style="left:64px;top:400px;width:952px;height:760px;">
        <div class="mono terracotta" style="font-size:28px;margin-bottom:20px;">BẢN CHẤT MỐI NGUY HIỂM</div>
        <div class="serif lbl" style="font-size:54px;">Sự nguy hiểm không nằm ở việc cỗ máy thông minh hơn...</div>
        <div class="serif terracotta" style="font-size:50px;font-weight:700;margin-top:24px;">Mà là con người tự nguyện lười suy nghĩ.</div>
        <div class="mono plum" style="margin-top:48px;font-size:28px;font-weight:700;">+ THEO DÕI TÂM TRÍ</div>
      </div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;

      // S1 (0-6s)
      tl.to("#sc1-card", {{ opacity: 1, duration: 0.6, ease: "power2.out" }}, 0.3);
      tl.to("#sc1-card", {{ opacity: 0, duration: 0.4 }}, 5.6);

      // S2 (6-12s)
      tl.to("#sc2-card", {{ opacity: 1, duration: 0.6, ease: "power2.out" }}, 6.0);
      tl.to("#sc2-card", {{ opacity: 0, duration: 0.4 }}, 11.6);

      // S3 (12-18s)
      tl.to("#sc3-card", {{ opacity: 1, duration: 0.6, ease: "power2.out" }}, 12.0);
    </script>
  </body>
</html>"""


def get_html_ban_co(duration: float = 17.0) -> str:
    return f"""<!doctype html>
<html lang="vi" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>BÀN CỜ — Big Tech Trái Phiếu AI CapEx</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600;700&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      :root{{--paper:#FAFAF7;--white:#FFFFFF;--ink:#1B2624;--green:#376B50;--gold:#B18D55;--rule:#E3E6E1;--font-sans:"Inter",sans-serif;--font-mono:"IBM Plex Mono",monospace;}}
      *{{margin:0;padding:0;box-sizing:border-box}}
      html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--paper);color:var(--ink);font-family:var(--font-sans);-webkit-font-smoothing:antialiased}}
      #root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--paper)}}
      .grid-backdrop{{position:absolute;inset:0;background-image:linear-gradient(to right,rgba(227,230,225,0.7) 1px,transparent 1px),linear-gradient(to bottom,rgba(227,230,225,0.7) 1px,transparent 1px);background-size:48px 48px;pointer-events:none}}
      .financial-header{{position:absolute;top:140px;left:64px;width:952px;height:84px;border-bottom:2px solid var(--ink);display:flex;align-items:center;justify-content:space-between;font-family:var(--font-mono);font-size:26px;font-weight:700}}
      .card{{position:absolute;background:rgba(255,255,255,0.92);backdrop-filter:blur(12px);border:1.5px solid var(--rule);border-radius:24px;box-shadow:0 12px 36px rgba(27,38,36,0.08);padding:44px;opacity:0}}
      .mono{{font-family:var(--font-mono)}}
      .num{{font-size:120px;font-weight:900;color:var(--green);letter-spacing:-0.03em;line-height:1;margin:16px 0}}
      .lbl{{font-size:46px;font-weight:800;line-height:1.2}}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-fps="30" data-duration="{duration}">
      <audio id="master-audio" src="assets/audio/final_mix.mp3" data-start="0" data-duration="{duration}" data-track-index="10" data-volume="1"></audio>
      <div class="grid-backdrop"></div>
      <div class="financial-header">
        <span>BÀN CỜ // THỊ TRƯỜNG VỐN DOANH NGHIỆP</span>
        <span style="color:var(--green)">BIG TECH CAPEX · 2026</span>
      </div>

      <!-- Scene 1: Corporate Debt Wave -->
      <div class="card" id="sc1-card" style="left:64px;top:380px;width:952px;height:760px;">
        <div class="mono" style="color:var(--green);font-size:28px;">CUỘC ĐUA TÀI TRỢ CHIP AI</div>
        <div class="lbl" style="margin-top:20px;">Big Tech Ồ Ạt Vay Nợ Qua Thị Trường Trái Phiếu</div>
        <p style="font-size:34px;color:#555;line-height:1.45;margin-top:28px;">Để theo kịp đà đầu tư hàng chục tỷ đô la cho chip GPU mỗi quý, các tập đoàn công nghệ hàng đầu chuyển hướng sang huy động nợ vay dài hạn.</p>
        <div class="mono" style="margin-top:36px;font-size:24px;color:#777;">SEC 10-K FILINGS // GAAP AUDITED DEBT METRICS</div>
      </div>

      <!-- Scene 2: $200B+ Record -->
      <div class="card" id="sc2-card" style="left:64px;top:380px;width:952px;height:820px;background:rgba(240,248,244,0.95);border-color:var(--green);">
        <div class="mono" style="color:var(--green);font-size:28px;">TỔNG KHỐI LƯỢNG PHÁT HÀNH</div>
        <div class="num">$200B+</div>
        <div class="lbl">Hơn Hai Trăm Tỷ Đô La Trái Phiếu Một Năm</div>
        <p style="font-size:34px;color:var(--ink);line-height:1.45;margin-top:20px;">Lượng phát hành trái phiếu doanh nghiệp lập kỷ lục mọi thời đại trong lịch sử Thung lũng Silicon.</p>
        <div class="mono" style="margin-top:32px;font-size:26px;color:var(--green);font-weight:700;">LÃI SUẤT DANH NGHĨA TRUNG BÌNH: 5.2% - 5.8%</div>
      </div>

      <!-- Scene 3: Capital Gamble Verdict -->
      <div class="card" id="sc3-card" style="left:64px;top:380px;width:952px;height:780px;">
        <div class="mono" style="color:var(--gold);font-size:28px;">BÀI TOÁN DÒNG TIỀN TỰ DO</div>
        <div class="lbl" style="font-size:50px;color:var(--ink);margin:24px 0;">Ván Cờ Đặt Cược Tương Lai</div>
        <p style="font-size:34px;color:#444;line-height:1.45;">Khi dòng tiền kinh doanh không còn đủ bù đắp CapEx, ván cờ tài chính bắt buộc các gã khổng lồ phải đặt cược toàn bộ bảng cân đối kế toán.</p>
        <div class="mono" style="margin-top:40px;font-size:28px;font-weight:700;color:var(--green);">+ THEO DÕI BÀN CỜ TÀI CHÍNH</div>
      </div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;

      // S1 (0-5.5s)
      tl.to("#sc1-card", {{ opacity: 1, duration: 0.5, ease: "power2.out" }}, 0.3);
      tl.to("#sc1-card", {{ opacity: 0, duration: 0.3 }}, 5.1);

      // S2 (5.5-11.5s)
      tl.to("#sc2-card", {{ opacity: 1, duration: 0.5, ease: "power2.out" }}, 5.5);
      tl.to("#sc2-card", {{ opacity: 0, duration: 0.3 }}, 11.1);

      // S3 (11.5-17s)
      tl.to("#sc3-card", {{ opacity: 1, duration: 0.5, ease: "power2.out" }}, 11.5);
    </script>
  </body>
</html>"""
