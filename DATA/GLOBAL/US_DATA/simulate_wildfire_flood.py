import random
import math

# ====== DỮ LIỆU THAM KHẢO ======
# Cháy rừng: 95,137 vụ/năm
# Lũ lụt: 70,000 sự kiện/năm
# Mô phỏng 5 năm (2021-2026) với biến động theo mùa

months = 60  # 5 năm
base_fire = 95137 / 12  # ~7,928 vụ/tháng
base_flood = 70000 / 12  # ~5,833 sự kiện/tháng

# Biến động theo mùa (mùa hè nhiều cháy, mùa xuân nhiều lũ)
seasonal_fire = [1.0, 0.8, 0.9, 1.1, 1.4, 1.8, 2.0, 1.9, 1.5, 1.2, 0.9, 0.7]
seasonal_flood = [1.3, 1.5, 1.7, 1.8, 1.6, 1.4, 1.1, 0.9, 0.8, 0.7, 0.9, 1.2]

# Tạo dữ liệu mô phỏng
actual_fires = []
actual_floods = []

for i in range(months):
    month = i % 12
    fire = int(base_fire * seasonal_fire[month] * random.uniform(0.85, 1.15))
    flood = int(base_flood * seasonal_flood[month] * random.uniform(0.85, 1.15))
    actual_fires.append(fire)
    actual_floods.append(flood)

# ====== TÍNH LAMBDA ======
lambda_fire = sum(actual_fires) / months
lambda_flood = sum(actual_floods) / months

# ====== DỰ BÁO POISSON ======
predicted_fires = lambda_fire * months
predicted_floods = lambda_flood * months

# ====== KẾT QUẢ ======
print("\n" + "="*70)
print("🔥 DỰ BÁO CHÁY RỪNG VÀ LŨ LỤT MỸ (MÔ PHỎNG 5 NĂM)")
print("="*70)

print(f"\n🔥 CHÁY RỪNG:")
print(f"   Tổng thực tế: {sum(actual_fires)}")
print(f"   Tổng dự báo: {predicted_fires:.0f}")
print(f"   Sai số: {abs(sum(actual_fires) - predicted_fires) / sum(actual_fires) * 100:.2f}%")
print(f"   λ: {lambda_fire:.2f} vụ/tháng")

print(f"\n🌊 LŨ LỤT:")
print(f"   Tổng thực tế: {sum(actual_floods)}")
print(f"   Tổng dự báo: {predicted_floods:.0f}")
print(f"   Sai số: {abs(sum(actual_floods) - predicted_floods) / sum(actual_floods) * 100:.2f}%")
print(f"   λ: {lambda_flood:.2f} sự kiện/tháng")

print("\n" + "="*70)
