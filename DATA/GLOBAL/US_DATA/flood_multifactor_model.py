# flood_multifactor_model.py
# Mô hình dự báo lũ lụt kết hợp ENSO, Mùa vụ, và Bão

# Dữ liệu lũ lụt tỷ đô (2016-2025)
floods = [2, 4, 2, 3, 3, 4, 2, 3, 4, 4]

# Chỉ số ENSO (El Niño = 1, La Niña = -1, Trung tính = 0)
enso = [0, 1, -1, 0, 1, -1, 0, 1, -1, 0]

# Số cơn bão đổ bộ vào Mỹ (2016-2025)
storms = [3, 5, 2, 4, 3, 6, 2, 3, 4, 5]

# ====== 1. TÍNH LAMBDA THEO NHÓM ======
def tinh_lambda_theo_dieu_kien(floods, storms, enso, condition):
    # condition: 'storms' hoặc 'enso'
    if condition == 'storms':
        # Chia thành 2 nhóm: bão nhiều (>=4) và bão ít (<4)
        floods_high = [floods[i] for i in range(len(floods)) if storms[i] >= 4]
        floods_low = [floods[i] for i in range(len(floods)) if storms[i] < 4]
        lambda_high = sum(floods_high) / len(floods_high) if floods_high else 0
        lambda_low = sum(floods_low) / len(floods_low) if floods_low else 0
        return lambda_high, lambda_low, 'bão nhiều', 'bão ít'
    
    elif condition == 'enso':
        floods_elnino = [floods[i] for i in range(len(floods)) if enso[i] >= 0.5]
        floods_normal = [floods[i] for i in range(len(floods)) if enso[i] < 0.5]
        lambda_elnino = sum(floods_elnino) / len(floods_elnino) if floods_elnino else 0
        lambda_normal = sum(floods_normal) / len(floods_normal) if floods_normal else 0
        return lambda_elnino, lambda_normal, 'El Niño', 'Không El Niño'

# ====== 2. TÍNH LAMBDA KẾT HỢP (BÃO + ENSO) ======
def tinh_lambda_ket_hop(floods, storms, enso):
    # Chia thành 4 nhóm
    groups = {}
    for i in range(len(floods)):
        storm_type = 'high' if storms[i] >= 4 else 'low'
        enso_type = 'elnino' if enso[i] >= 0.5 else 'normal'
        key = f"{storm_type}_{enso_type}"
        if key not in groups:
            groups[key] = []
        groups[key].append(floods[i])
    
    lambdas = {}
    for key, values in groups.items():
        lambdas[key] = sum(values) / len(values) if values else 0
    
    return lambdas

# ====== 3. CHẠY MÔ HÌNH ======
print("\n" + "="*60)
print("📊 DỰ BÁO LŨ LỤT VỚI ĐA YẾU TỐ")
print("="*60)

# Theo bão
lambda_high, lambda_low, name1, name2 = tinh_lambda_theo_dieu_kien(floods, storms, enso, 'storms')
print(f"\n🔹 Theo số lượng bão:")
print(f"   λ cho năm {name1}: {lambda_high:.2f} sự kiện/năm")
print(f"   λ cho năm {name2}: {lambda_low:.2f} sự kiện/năm")

# Theo ENSO
lambda_elnino, lambda_normal, name1, name2 = tinh_lambda_theo_dieu_kien(floods, storms, enso, 'enso')
print(f"\n🔹 Theo ENSO:")
print(f"   λ cho năm {name1}: {lambda_elnino:.2f} sự kiện/năm")
print(f"   λ cho năm {name2}: {lambda_normal:.2f} sự kiện/năm")

# Kết hợp
lambdas = tinh_lambda_ket_hop(floods, storms, enso)
print(f"\n🔹 Kết hợp bão + ENSO:")
for key, val in lambdas.items():
    print(f"   λ cho {key}: {val:.2f} sự kiện/năm")
