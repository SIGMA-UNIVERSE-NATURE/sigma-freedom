import json
import math

# Đọc dữ liệu động đất Mỹ
with open('DATA/GLOBAL/US_DATA/EARTHQUAKES/us_earthquakes_2021_2026.geojson', 'r') as f:
    data = json.load(f)

# Trích xuất cường độ động đất (mag)
magnitudes = []
for feature in data['features']:
    mag = feature['properties'].get('mag')
    if mag is not None:
        magnitudes.append(mag)

# Phân loại theo ngưỡng
thresholds = [3.5, 4.0, 4.5, 5.0, 5.5]
actual_counts = {}
for th in thresholds:
    actual_counts[th] = len([m for m in magnitudes if m >= th])

# Dự báo Poisson (λ = 28 cho M≥4.5)
lambda_base = 28
lambda_est = {
    3.5: lambda_base * 5.0,
    4.0: lambda_base * 2.5,
    4.5: lambda_base,
    5.0: lambda_base * 0.3,
    5.5: lambda_base * 0.1,
}

print("="*60)
print("📊 SO SÁNH DỰ BÁO POISSON VỚI DỮ LIỆU ĐỘNG ĐẤT MỸ (2021-2026)")
print("="*60)

for th in thresholds:
    actual = actual_counts[th]
    predicted = lambda_est[th] * 12 * 5  # 5 năm, 12 tháng/năm
    error = abs(actual - predicted) / actual * 100 if actual > 0 else 0
    print(f"\n🔹 Ngưỡng M ≥ {th}:")
    print(f"   Số lượng thực tế: {actual}")
    print(f"   Số lượng dự báo:  {predicted:.0f}")
    print(f"   Sai số:          {error:.2f}%")
