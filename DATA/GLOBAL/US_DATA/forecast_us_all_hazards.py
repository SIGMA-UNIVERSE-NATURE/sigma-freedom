import json
import math
from datetime import datetime

# ====== THAM SỐ LAMBDA TỐI ƯU CHO TỪNG LOẠI THIÊN TAI MỸ ======
lambda_us = {
    "earthquake": {
        3.5: 27.0167,
        4.0: 9.7500,
        4.5: 3.0500,
        5.0: 0.9000,
        5.5: 0.2167
    },
    "wildfire": {
        "avg": 61500/12,  # vụ/tháng (từ NIFC 10 năm)
        "seasonal": [1.0, 0.8, 0.9, 1.1, 1.4, 1.8, 2.0, 1.9, 1.5, 1.2, 0.9, 0.7]
    },
    "flood": {
        "avg": 1.7,  # sự kiện tỷ đô/năm (từ NOAA)
        "seasonal": [1.3, 1.5, 1.7, 1.8, 1.6, 1.4, 1.1, 0.9, 0.8, 0.7, 0.9, 1.2]
    }
}

# ====== DỰ BÁO POISSON ======
def poisson_forecast(lambda_val, months):
    return lambda_val * months

# ====== DỰ BÁO THEO MÙA ======
def seasonal_forecast(lambda_avg, seasonal_factor, months):
    total = 0
    for i in range(months):
        month = i % 12
        total += lambda_avg * seasonal_factor[month]
    return total

# ====== IN BẢNG DỰ BÁO ======
print("\n" + "="*80)
print("🌍 DỰ BÁO THIÊN TAI MỸ - 12 THÁNG TỚI (2026-2027)")
print("="*80)
print("\nDựa trên λ tối ưu từ dữ liệu thực tế (2021-2026)\n")

# 1. ĐỘNG ĐẤT
print("\n🔹 ĐỘNG ĐẤT:")
print(f"{'Tháng':<6} {'M≥3.5':<10} {'M≥4.0':<10} {'M≥4.5':<10} {'M≥5.0':<10} {'M≥5.5':<10}")
print("-"*60)
for month in range(1, 13):
    row = f"{month:<6}"
    for th in sorted(lambda_us["earthquake"].keys()):
        count = poisson_forecast(lambda_us["earthquake"][th], month)
        row += f"{count:<10.0f}"
    print(row)

# 2. CHÁY RỪNG
print("\n🔹 CHÁY RỪNG:")
lambda_fire_avg = lambda_us["wildfire"]["avg"]
print(f"   Số vụ dự kiến (12 tháng): {seasonal_forecast(lambda_fire_avg, lambda_us['wildfire']['seasonal'], 12):.0f} vụ")
print(f"   Cao điểm: Tháng 7-9 (mùa hè)")

# 3. LŨ LỤT
print("\n🔹 LŨ LỤT:")
lambda_flood_avg = lambda_us["flood"]["avg"]
print(f"   Số sự kiện tỷ đô dự kiến (12 tháng): {seasonal_forecast(lambda_flood_avg, lambda_us['flood']['seasonal'], 12):.1f} sự kiện")
print(f"   Cao điểm: Tháng 3-6 (mùa xuân)")

# 4. TỔNG KẾT
print("\n" + "="*80)
print("📌 TỔNG KẾT 12 THÁNG:")
print("   Động đất: ~324 trận (M≥3.5), ~117 trận (M≥4.0), ~37 trận (M≥4.5)")
print(f"   Cháy rừng: ~{seasonal_forecast(lambda_fire_avg, lambda_us['wildfire']['seasonal'], 12):.0f} vụ")
print(f"   Lũ lụt: ~{seasonal_forecast(lambda_flood_avg, lambda_us['flood']['seasonal'], 12):.1f} sự kiện tỷ đô")
print("="*80)
