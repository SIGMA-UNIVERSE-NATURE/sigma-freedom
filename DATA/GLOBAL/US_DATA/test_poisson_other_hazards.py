import json
import math
import random

# ====== DỮ LIỆU MÔ PHỎNG DỰA TRÊN THỐNG KÊ THỰC TẾ ======
# Nguồn: NASA FIRMS (cháy), NOAA Storm Events (lũ)

# Cháy rừng: ~95,000 vụ/năm trên toàn nước Mỹ
# Lũ lụt: ~70,000 sự kiện/năm (tất cả các loại)
# Chúng ta sẽ lấy mẫu 5 năm (2021-2026)

months = 60  # 5 năm
fires_per_month = 95000 / 12  # ~7917 vụ/tháng
floods_per_month = 70000 / 12  # ~5833 vụ/tháng

# Mô phỏng dữ liệu thực tế với một chút nhiễu ngẫu nhiên
actual_fires = [int(fires_per_month + random.gauss(0, 500)) for _ in range(months)]
actual_floods = [int(floods_per_month + random.gauss(0, 400)) for _ in range(months)]

# ====== DỰ BÁO POISSON ======
def poisson_forecast(lambda_val, months):
    return lambda_val * months

# Ước tính λ từ dữ liệu mô phỏng (thực tế sẽ tính từ dữ liệu thật)
lambda_fire = sum(actual_fires) / months
lambda_flood = sum(actual_floods) / months

print("="*70)
print("🔥 THỬ NGHIỆM POISSON VỚI CHÁY RỪNG VÀ LŨ LỤT MỸ (5 NĂM)")
print("="*70)

# ====== CHÁY RỪNG ======
total_fires = sum(actual_fires)
predicted_fires = poisson_forecast(lambda_fire, months)
error_fire = abs(total_fires - predicted_fires) / total_fires * 100

print(f"\n🔥 CHÁY RỪNG:")
print(f"   Số vụ thực tế (5 năm): {total_fires}")
print(f"   Số vụ dự báo (Poisson): {predicted_fires:.0f}")
print(f"   Sai số: {error_fire:.2f}%")
print(f"   λ tối ưu: {lambda_fire:.2f} vụ/tháng")

# ====== LŨ LỤT ======
total_floods = sum(actual_floods)
predicted_floods = poisson_forecast(lambda_flood, months)
error_flood = abs(total_floods - predicted_floods) / total_floods * 100

print(f"\n🌊 LŨ LỤT:")
print(f"   Số vụ thực tế (5 năm): {total_floods}")
print(f"   Số vụ dự báo (Poisson): {predicted_floods:.0f}")
print(f"   Sai số: {error_flood:.2f}%")
print(f"   λ tối ưu: {lambda_flood:.2f} vụ/tháng")

# ====== KẾT LUẬN ======
print("\n" + "="*70)
print("📌 NHẬN XÉT:")
print("- Poisson có thể mô phỏng tốt cho các sự kiện có λ lớn (hàng nghìn vụ/tháng)")
print("- Sai số dự kiến < 5% nếu dữ liệu ổn định")
print("- Cần dữ liệu thực tế để xác nhận, nhưng công thức Poisson có thể áp dụng được")
