#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
sigma_standardized.py
Mô hình chuẩn hóa λ theo ma trận thiên tai - Trách nhiệm và Nhân ái
"""

import json
import math
import pandas as pd

# ====== 1. ĐỌC DỮ LIỆU λ THÔ ======
print("\n📂 Đang đọc dữ liệu λ từ lambda_global.json...")
with open('DATA/PARAMETERS/lambda_global.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# ====== 2. XÁC ĐỊNH DANH SÁCH QUỐC GIA CẦN XỬ LÝ ======
countries = list(raw_data['regions'].keys())
print(f"✅ Đã tìm thấy {len(countries)} quốc gia/khu vực.")

# ====== 3. TẠO MA TRẬN THIÊN TAI CHO TỪNG QUỐC GIA ======
hazard_keys = {
    'flood': 0.20,
    'typhoon': 0.18,
    'hurricane': 0.18,
    'earthquake': 0.15,
    'wildfire': 0.12,
    'drought': 0.10,
    'landslide': 0.08,
    'tornado': 0.05,
    'heatwave': 0.05,
    'winter_storm': 0.04,
    'tsunami': 0.03
}

# Mặc định trọng số 0.1 cho các loại thiên tai khác
DEFAULT_WEIGHT = 0.1

# ====== 4. CHUẨN HÓA VÀ TÍNH TOÁN ======
results = []

for country, hazards in raw_data['regions'].items():
    # Bỏ qua các khu vực tổng hợp (sea, europe)
    if country in ['sea', 'europe']:
        continue

    # Tổng hợp λ từ các loại thiên tai
    total_lambda = 0
    total_weight = 0
    hazard_details = {}

    for hazard, value in hazards.items():
        if isinstance(value, dict) and 'lambda' in value:
            raw_lambda = value['lambda']
            # Gán trọng số theo loại thiên tai
            weight = hazard_keys.get(hazard, DEFAULT_WEIGHT)
            # Chuẩn hóa nội bộ: chia cho 100 (hoặc giá trị đặc trưng)
            normalized = raw_lambda / 100 if isinstance(raw_lambda, (int, float)) else 0
            total_lambda += normalized * weight
            total_weight += weight
            hazard_details[hazard] = normalized

    # Trung bình có trọng số
    if total_weight > 0:
        lambda_final = total_lambda / total_weight
    else:
        lambda_final = 0

    results.append({
        'Country': country,
        'Lambda_Raw': lambda_final,
        'Details': hazard_details
    })

# ====== 5. CHUẨN HÓA VỀ THANG 0-100 ======
df = pd.DataFrame(results)
if not df.empty:
    min_lambda = df['Lambda_Raw'].min()
    max_lambda = df['Lambda_Raw'].max()
    if max_lambda > min_lambda:
        df['SIGMA_Index'] = ((df['Lambda_Raw'] - min_lambda) / (max_lambda - min_lambda)) * 100
    else:
        df['SIGMA_Index'] = 0

# ====== 6. XUẤT KẾT QUẢ ======
print("\n" + "="*80)
print("       🌍 CHỈ SỐ RỦI RO THIÊN TAI SIGMA (MA TRẬN CHUẨN HÓA)       ")
print("="*80)
print(f"{'Quốc gia':<15} | {'λ tổng hợp':<12} | {'SIGMA Index':<13}")
print("-"*60)

df_sorted = df.sort_values(by='SIGMA_Index', ascending=False)
for _, row in df_sorted.iterrows():
    print(f"{row['Country']:<15} | {row['Lambda_Raw']:<12.4f} | {row['SIGMA_Index']:<13.2f}")

print("="*80)

# ====== 7. LƯU FILE CSV ======
df_sorted.to_csv('SIGMA_Standardized_Report.csv', index=False)
print("\n✅ Đã xuất file: SIGMA_Standardized_Report.csv")
print("🕊️ Món quà miễn phí có giá trị đang được hoàn thiện...")
