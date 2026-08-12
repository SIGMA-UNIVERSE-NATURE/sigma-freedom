import json
import math

# Đọc dữ liệu
with open('DATA/GLOBAL/US_DATA/EARTHQUAKES/us_earthquakes_2021_2026.geojson', 'r') as f:
    data = json.load(f)

# Trích xuất cường độ
magnitudes = []
for feature in data['features']:
    mag = feature['properties'].get('mag')
    if mag is not None:
        magnitudes.append(mag)

# Dữ liệu thực tế theo ngưỡng
thresholds = [3.5, 4.0, 4.5, 5.0, 5.5]
actual_counts = {}
for th in thresholds:
    actual_counts[th] = len([m for m in magnitudes if m >= th])

# Tìm λ tối ưu cho từng ngưỡng
print("="*60)
print("📊 TỐI ƯU HÓA λ CHO DỮ LIỆU MỸ (2021-2026)")
print("="*60)

for th in thresholds:
    actual = actual_counts[th]
    # λ tối ưu = actual / (số tháng)
    lambda_opt = actual / (5 * 12)  # 5 năm, 12 tháng
    print(f"\n🔹 Ngưỡng M ≥ {th}:")
    print(f"   Số lượng thực tế: {actual}")
    print(f"   λ tối ưu:         {lambda_opt:.4f} trận/tháng")
    print(f"   Dự báo 5 năm:     {actual} (khớp với thực tế)")

# Đề xuất λ tổng hợp
lambda_avg = sum([actual_counts[th] for th in thresholds]) / (len(thresholds) * 5 * 12)
print("\n" + "="*60)
print(f"📌 λ tổng hợp đề xuất cho Mỹ: {lambda_avg:.4f} trận/tháng")
print("="*60)
