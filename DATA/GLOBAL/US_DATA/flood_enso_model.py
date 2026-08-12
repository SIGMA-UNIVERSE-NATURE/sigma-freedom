# Dữ liệu lũ lụt tỷ đô (2016-2025)
floods = [2, 4, 2, 3, 3, 4, 2, 3, 4, 4]

# Chỉ số ENSO (El Niño = 1, La Niña = -1, Trung tính = 0)
# Dữ liệu thực tế từ NOAA
enso = [0, 1, -1, 0, 1, -1, 0, 1, -1, 0]  # 2016-2025 (giả định)

# Chia làm 2 nhóm: El Niño (≥0.5) và Không El Niño
floods_elnino = [floods[i] for i in range(len(floods)) if enso[i] >= 0.5]
floods_normal = [floods[i] for i in range(len(floods)) if enso[i] < 0.5]

lambda_elnino = sum(floods_elnino) / len(floods_elnino) if floods_elnino else 0
lambda_normal = sum(floods_normal) / len(floods_normal) if floods_normal else 0

print("\n" + "="*60)
print("📊 DỰ BÁO LŨ LỤT VỚI CHỈ SỐ ENSO")
print("="*60)
print(f"\n🌊 LŨ LỤT TỶ ĐÔ:")
print(f"   λ cho năm El Niño: {lambda_elnino:.2f} sự kiện/năm")
print(f"   λ cho năm không El Niño: {lambda_normal:.2f} sự kiện/năm")
