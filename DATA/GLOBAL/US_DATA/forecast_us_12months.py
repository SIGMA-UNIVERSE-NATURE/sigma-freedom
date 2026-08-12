import json
import math
from datetime import datetime, timedelta

# ====== THAM SỐ LAMBDA TỐI ƯU CHO MỸ ======
lambda_us = {
    3.5: 27.0167,
    4.0: 9.7500,
    4.5: 3.0500,
    5.0: 0.9000,
    5.5: 0.2167
}

# ====== DỰ BÁO POISSON ======
def poisson_forecast(lambda_val, months):
    return lambda_val * months

# ====== IN BẢNG DỰ BÁO ======
print("\n" + "="*70)
print("🌍 DỰ BÁO ĐỘNG ĐẤT MỸ - 12 THÁNG TỚI")
print("="*70)
print("\nDựa trên λ tối ưu từ dữ liệu 2021-2026\n")

# Header
print(f"{'Tháng':<6} {'M≥3.5':<10} {'M≥4.0':<10} {'M≥4.5':<10} {'M≥5.0':<10} {'M≥5.5':<10}")
print("-"*60)

# Dự báo từng tháng
for month in range(1, 13):
    row = f"{month:<6}"
    for th in sorted(lambda_us.keys()):
        count = poisson_forecast(lambda_us[th], month)
        row += f"{count:<10.0f}"
    print(row)

# Dự báo theo quý
print("\n" + "="*70)
print("📊 DỰ BÁO THEO QUÝ")
print("="*70)

quarters = [(1,3), (4,6), (7,9), (10,12)]
for q_start, q_end in quarters:
    months = q_end - q_start + 1
    print(f"\n🔹 Quý {q_start}-{q_end}:")
    for th in sorted(lambda_us.keys()):
        count = poisson_forecast(lambda_us[th], months)
        print(f"   M≥{th}: {count:.0f} trận")

# Tổng kết 12 tháng
print("\n" + "="*70)
print("📌 TỔNG KẾT 12 THÁNG")
print("="*70)
for th in sorted(lambda_us.keys()):
    total = poisson_forecast(lambda_us[th], 12)
    print(f"   M≥{th}: {total:.0f} trận dự kiến")
