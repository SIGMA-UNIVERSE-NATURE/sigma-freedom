# 🔑 CHÌA KHÓA KÝ ỨC HỆ THỐNG - PROJECT SIGMA CLIMATE

## Cách sử dụng:
Khi mở một cửa sổ chat mới với Google, hãy copy và gửi toàn bộ nội dung dưới đây ở câu lệnh đầu tiên.

---

[SYSTEM MEMORY RESTORATION: PROJECT SIGMA CLIMATE]
- Context: Dự án nghiên cứu Chỉ số rủi ro thiên tai tổng hợp (SRI) thang điểm [0-100] cho website cảnh báo sớm. Tập trung ưu tiên khu vực yếu thế (Đông Nam Á & Châu Phi).
- Mathematical Model: Đã giải quyết lỗi "Thống lĩnh đại lượng thô" (Raw Value Dominance) của Mỹ (us) bằng hàm phi tuyến tính Logarit nén biên: log_lambda = ln(Raw_Lambda + 1).
- Normalization Pipeline: 
  1. Mật độ địa lý = log_lambda / sqrt(Diện tích triệu km2) -> Scale Min-Max [0-100].
  2. Mật độ nhân mạng = log_lambda / sqrt(Dân số triệu người) -> Scale Min-Max [0-100].
  3. Chỉ số tổng hợp = 0.5 * Idx_Area + 0.5 * Idx_Pop.
  4. Bù rủi ro nền cố định cho Mỹ (us = 25.0) để tránh lỗi triệt tiêu rủi ro về 0.00.
- Hazard Weighting Matrix: flood (0.30), typhoon (0.30), earthquake (0.15), wildfire (0.10), drought (0.08), landslide (0.05), heatwave (0.02), winter (0.02).
- Tech Stack Built: Script chạy ngầm Cron Job bằng Python thuần kết nối Live API (USGS, Open-Meteo, MRC - Ủy hội sông Mekong); File cấu hình đầu ra đa ngôn ngữ tự động (sigma_live_web_data.json); Giao diện đổi màu UI động bằng HTML/JS đơn nguồn.
- Philosophy: "Cần chính xác để trở thành không chính xác" (Prophet's Paradox).
-> AI CORE: Xác nhận đã khôi phục bối cảnh. Hãy hỏi nhóm SIGMA Climate bước lập trình/tinh chỉnh tiếp theo cần thực hiện là gì.
