"""Channel Specifications for CofVid E2E Pipeline Testing.

Defines the 5 channel configs, research data, scripts, scene plans,
and HyperFrames HTML compositions for:
1. e2e-mach-so (Mạch Số)
2. e2e-van-vat (Vạn Vật)
3. e2e-dau-moc (Dấu Mốc)
4. e2e-tam-tri (Tâm Trí)
5. e2e-ban-co (Bàn Cờ)
"""

from __future__ import annotations
from typing import Any, Dict

CHANNELS: Dict[str, Dict[str, Any]] = {
    "e2e-mach-so": {
        "channel": "mach-so",
        "title": "Mạch Số — Cảnh Báo Gartner: 3.5 Nghìn Tỷ USD Hạ Tầng AI",
        "topic": "Cảnh báo của Gartner: 3.5 nghìn tỷ USD hạ tầng AI và nghịch lý ROI điện năng",
        "playbook": "mach-so",
        "voice": "Hải Đăng",
        "music_track": "Cool Vibes.mp3",
        "research_url": "https://www.gartner.com/en/newsroom/press-releases/2024-11-19-gartner-says-more-than-40-percent-of-ai-data-centers-will-be-operationally-constrained-by-power-availability-by-2027",
        "target_duration": 16.0,
        "script_text": "Gartner vừa phát đi cảnh báo đỏ: Ba nghìn năm trăm tỷ đô la đang đổ vào hạ tầng AI. Nghịch lý ở đâu? Tám mươi lăm phần trăm trung tâm dữ liệu mới sẽ thiếu điện trước năm 2027. Khi chi phí điện năng vượt cả doanh thu mô hình, bài toán lợi nhuận AI chính thức vỡ trận.",
        "scenes": [
            {
                "id": "sc01",
                "type": "stat_card",
                "label": "Hook — $3.5T USD CapEx",
                "text": "Gartner vừa phát đi cảnh báo đỏ: Ba nghìn năm trăm tỷ đô la đang đổ vào hạ tầng AI.",
                "start": 0.0,
                "end": 5.0,
                "banner_title": "CẢNH BÁO // GARTNER",
                "slot_idx": 1,
                "latency_val": "12 ms",
                "latency_color": "#10B981"
            },
            {
                "id": "sc02",
                "type": "comparison",
                "label": "Build — Nghịch lý thiếu điện",
                "text": "Nghịch lý ở đâu? Tám mươi lăm phần trăm trung tâm dữ liệu mới sẽ thiếu điện trước năm 2027.",
                "start": 5.0,
                "end": 11.0,
                "banner_title": "NGHỊCH LÝ // THIẾU ĐIỆN",
                "slot_idx": 2,
                "latency_val": "480 ms",
                "latency_color": "#FF4757"
            },
            {
                "id": "sc03",
                "type": "text_card",
                "label": "Landing — Vỡ trận lợi nhuận",
                "text": "Khi chi phí điện năng vượt cả doanh thu mô hình, bài toán lợi nhuận AI chính thức vỡ trận.",
                "start": 11.0,
                "end": 16.0,
                "banner_title": "KẾT LUẬN // ROI ÂM",
                "slot_idx": 3,
                "latency_val": "16 ms",
                "latency_color": "#10B981"
            }
        ]
    },
    "e2e-van-vat": {
        "channel": "van-vat",
        "title": "Vạn Vật — Kính Thiên Văn IceCube Phát Hiện Neutrino Nam Cực",
        "topic": "Kính thiên văn IceCube phát hiện Neutrino năng lượng cao tại Nam Cực",
        "playbook": "van-vat",
        "voice": "Mai Anh",
        "music_track": "The Complex.mp3",
        "research_url": "https://icecube.wisc.edu/",
        "target_duration": 19.0,
        "script_text": "Dưới hai nghìn năm trăm mét băng vĩnh cửu Nam Cực, một cỗ máy săn hạt vô hình đang hoạt động. Đài quan sát IceCube vừa ghi nhận một hạt neutrino mang năng lượng một trăm tera electron volt. Tia sáng xanh Cherenkov lóe lên trong bóng tối, mở toang cửa sổ nhìn thẳng vào hố đen vũ trụ.",
        "scenes": [
            {
                "id": "sc01",
                "type": "diagram",
                "label": "Hook — Đài quan sát băng vĩnh cửu",
                "text": "Dưới hai nghìn năm trăm mét băng vĩnh cửu Nam Cực, một cỗ máy săn hạt vô hình đang hoạt động.",
                "start": 0.0,
                "end": 6.0,
                "banner_title": "ICECUBE // NAM CỰC",
                "slot_idx": 1
            },
            {
                "id": "sc02",
                "type": "stat_card",
                "label": "Build — Bắt giữ hạt 100 TeV",
                "text": "Đài quan sát IceCube vừa ghi nhận một hạt neutrino mang năng lượng một trăm tera electron volt.",
                "start": 6.0,
                "end": 12.0,
                "banner_title": "PHÁT HIỆN // 100 TEV",
                "slot_idx": 2
            },
            {
                "id": "sc03",
                "type": "text_card",
                "label": "Landing — Ánh sáng Cherenkov",
                "text": "Tia sáng xanh Cherenkov lóe lên trong bóng tối, mở toang cửa sổ nhìn thẳng vào hố đen vũ trụ.",
                "start": 12.0,
                "end": 19.0,
                "banner_title": "BỨC XẠ // CHERENKOV",
                "slot_idx": 3
            }
        ]
    },
    "e2e-dau-moc": {
        "channel": "dau-moc",
        "title": "Dấu Mốc — 13 Ngày Khủng Hoảng Tên Lửa Cuba 1962 & U-2",
        "topic": "13 ngày Khủng hoảng Tên lửa Cuba 1962 & Chuyến bay do thám U-2",
        "playbook": "dau-moc",
        "voice": "Hải Đăng",
        "music_track": "Impact Moderato.mp3",
        "research_url": "https://en.wikipedia.org/wiki/Cuban_Missile_Crisis",
        "target_duration": 17.0,
        "script_text": "Mười bốn tháng Mười một chín sáu hai: Chiếc máy bay do thám U-2 chụp được tấm ảnh thay đổi lịch sử. Bệ phóng tên lửa hạt nhân Liên Xô lộ diện tại San Cristóbal, chỉ cách bờ biển Mỹ một trăm bốn mươi cây số. Mười ba ngày nghẹt thở bắt đầu, nơi một quyết định sai lầm có thể xóa sổ hàng triệu sinh mạng.",
        "scenes": [
            {
                "id": "sc01",
                "type": "text_card",
                "label": "Hook — Tấm ảnh U-2 định mệnh",
                "text": "Mười bốn tháng Mười một chín sáu hai: Chiếc máy bay do thám U-2 chụp được tấm ảnh thay đổi lịch sử.",
                "start": 0.0,
                "end": 5.5,
                "banner_title": "DO THÁM U-2 // 1962",
                "slot_idx": 1
            },
            {
                "id": "sc02",
                "type": "diagram",
                "label": "Build — Bản đồ tên lửa San Cristóbal",
                "text": "Bệ phóng tên lửa hạt nhân Liên Xô lộ diện tại San Cristóbal, chỉ cách bờ biển Mỹ một trăm bốn mươi cây số.",
                "start": 5.5,
                "end": 11.5,
                "banner_title": "BẢN ĐỒ // CUBA 1962",
                "slot_idx": 2
            },
            {
                "id": "sc03",
                "type": "stat_card",
                "label": "Landing — 13 ngày nghẹt thở",
                "text": "Mười ba ngày nghẹt thở bắt đầu, nơi một quyết định sai lầm có thể xóa sổ hàng triệu sinh mạng.",
                "start": 11.5,
                "end": 17.0,
                "banner_title": "13 NGÀY // NGUY CƠ",
                "slot_idx": 3
            }
        ]
    },
    "e2e-tam-tri": {
        "channel": "tam-tri",
        "title": "Tâm Trí — Hiện Tượng Deference to AI: Nhượng Bộ Thuật Toán",
        "topic": "Hiện tượng tâm lý Deference to AI — Sự nhượng bộ vô thức của con người trước thuật toán",
        "playbook": "tam-tri",
        "voice": "Mai Anh",
        "music_track": "Heartbreaking.mp3",
        "research_url": "https://en.wikipedia.org/wiki/Automation_bias",
        "target_duration": 18.0,
        "script_text": "Bạn có nhận ra, chúng ta đang dần ngừng đặt câu hỏi trước mỗi câu trả lời của AI? Tâm lý học gọi đây là hiện tượng nhượng bộ thuật toán: khi bộ não tự động tắt cơ chế phản biện. Sự nguy hiểm không nằm ở việc cỗ máy thông minh hơn, mà là con người tự nguyện lười suy nghĩ.",
        "scenes": [
            {
                "id": "sc01",
                "type": "text_card",
                "label": "Hook — Ngừng đặt câu hỏi",
                "text": "Bạn có nhận ra, chúng ta đang dần ngừng đặt câu hỏi trước mỗi câu trả lời của AI?",
                "start": 0.0,
                "end": 6.0,
                "banner_title": "TÂM LÝ // ĐẶT CÂU HỎI",
                "slot_idx": 1
            },
            {
                "id": "sc02",
                "type": "comparison",
                "label": "Build — Cơ chế nhượng bộ thuật toán",
                "text": "Tâm lý học gọi đây là hiện tượng nhượng bộ thuật toán: khi bộ não tự động tắt cơ chế phản biện.",
                "start": 6.0,
                "end": 12.0,
                "banner_title": "DEFERENCE TO AI",
                "slot_idx": 2
            },
            {
                "id": "sc03",
                "type": "stat_card",
                "label": "Landing — Lười suy nghĩ tự nguyện",
                "text": "Sự nguy hiểm không nằm ở việc cỗ máy thông minh hơn, mà là con người tự nguyện lười suy nghĩ.",
                "start": 12.0,
                "end": 18.0,
                "banner_title": "CẢNH BÁO // TỰ NGUYỆN",
                "slot_idx": 3
            }
        ]
    },
    "e2e-ban-co": {
        "channel": "ban-co",
        "title": "Bàn Cờ — Big Tech và Cơn Sốt Trái Phiếu AI CapEx Trăm Tỷ USD",
        "topic": "Cơn sốt phát hành trái phiếu AI CapEx hàng trăm tỷ USD của Big Tech",
        "playbook": "ban-co",
        "voice": "Hải Đăng",
        "music_track": "Prelude and Action.mp3",
        "research_url": "https://en.wikipedia.org/wiki/Corporate_bond",
        "target_duration": 17.0,
        "script_text": "Để tài trợ cho cuộc đua chip AI, Big Tech đang ồ ạt vay mượn qua thị trường trái phiếu doanh nghiệp. Hơn hai trăm tỷ đô la trái phiếu được phát hành chỉ trong một năm, thiết lập kỷ lục nợ vay mọi thời đại. Khi dòng tiền tự do cạn kiệt, ván cờ tài chính bắt buộc các gã khổng lồ phải đặt cược tương lai.",
        "scenes": [
            {
                "id": "sc01",
                "type": "stat_card",
                "label": "Hook — Vay mượn đua chip",
                "text": "Để tài trợ cho cuộc đua chip AI, Big Tech đang ồ ạt vay mượn qua thị trường trái phiếu doanh nghiệp.",
                "start": 0.0,
                "end": 5.5,
                "banner_title": "BIG TECH // CAPEX",
                "slot_idx": 1
            },
            {
                "id": "sc02",
                "type": "comparison",
                "label": "Build — Kỷ lục $200B nợ vay",
                "text": "Hơn hai trăm tỷ đô la trái phiếu được phát hành chỉ trong một năm, thiết lập kỷ lục nợ vay mọi thời đại.",
                "start": 5.5,
                "end": 11.5,
                "banner_title": "TRÁI PHIẾU // $200B+",
                "slot_idx": 2
            },
            {
                "id": "sc03",
                "type": "text_card",
                "label": "Landing — Đặt cược tương lai",
                "text": "Khi dòng tiền tự do cạn kiệt, ván cờ tài chính bắt buộc các gã khổng lồ phải đặt cược tương lai.",
                "start": 11.5,
                "end": 17.0,
                "banner_title": "VÁN CỜ // ĐẶT CƯỢC",
                "slot_idx": 3
            }
        ]
    }
}
