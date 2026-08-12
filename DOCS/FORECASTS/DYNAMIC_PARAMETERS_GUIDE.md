# 🌍 HỆ THỐNG THAM SỐ ĐỘNG SIGMA CLIMATE

## Nguyên tắc
1. λ được tính toán lại hàng tháng từ dữ liệu mới nhất.
2. Dự báo được cập nhật tự động mỗi khi có dữ liệu mới.
3. Sai số được công bố kèm theo mỗi dự báo.

## Cấu trúc dữ liệu
- Mỗi khu vực có một file JSON riêng.
- Mỗi file chứa:
  - λ cho từng loại thiên tai
  - Hệ số mùa
  - Hệ số ENSO
  - Hệ số bão

## Cập nhật tự động
- Script chạy hàng tuần để tải dữ liệu mới.
- Tính λ mới và cập nhật vào file JSON.
- Đẩy lên GitHub và website.

## Kế hoạch phát triển
1. Viết script `update_lambda.py`
2. Thiết lập cron job (nếu có)
3. Tích hợp vào website
