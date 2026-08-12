#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
run_lambda.py
Tính toán λ tổng hợp theo ma trận thiên tai
Phiên bản nhẹ, không dùng pandas
"""

import json
import csv

# ====== TRỌNG SỐ CHUẨN ======
WEIGHTS = {
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
DEFAULT_WEIGHT = 0.10

# ====== ĐỌC DỮ LIỆU ======
print("\n📂 Đang đọc dữ liệu lambda_global.json...")

try:
    with open('DATA/PARAMETERS/lambda_global.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("❌ Không tìm thấy file lambda_global.json")
    exit(1)

regions = data.get('regions', {})

# ====== TÍNH TOÁN ======
results = []
for country, hazards in regions.items():
    if country in ['sea', 'europe']:
        continue

    total_weighted = 0
    total_weight = 0

    for hazard, value in hazards.items():
        if isinstance(value, dict) and 'lambda' in value:
            raw_val = value['lambda']
            if isinstance(raw_val, (int, float)):
                normalized = raw_val / 100.0
                weight = WEIGHTS.get(hazard, DEFAULT_WEIGHT)
                total_weighted += normalized * weight
                total_weight += weight

    lambda_avg = total_weighted / total_weight if total_weight > 0 else 0
    results.append({'country': country, 'lambda': lambda_avg})

# ====== CHUẨN HÓA ======
lambda_values = [r['lambda'] for r in results]
min_val = min(lambda_values) if lambda_values else 0
max_val = max(lambda_values) if lambda_values else 1
range_val = max_val - min_val

if range_val > 0:
    for r in results:
        r['sigma_index'] = ((r['lambda'] - min_val) / range_val) * 100
else:
    for r in results:
        r['sigma_index'] = 0

results.sort(key=lambda x: x['sigma_index'], reverse=True)

# ====== XUẤT KẾT QUẢ ======
print("\n" + "="*80)
print("       🌍 CHỈ SỐ RỦI RO THIÊN TAI SIGMA       ")
print("="*80)
print(f"{'Quốc gia':<15} | {'λ tổng hợp':<12} | {'SIGMA Index':<13}")
print("-"*60)

for r in results:
    print(f"{r['country']:<15} | {r['lambda']:<12.4f} | {r['sigma_index']:<13.2f}")

print("="*80)

# ====== LƯU FILE ======
with open('LAMBDA_FINAL_REPORT.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Country', 'Lambda', 'SIGMA_Index'])
    for r in results:
        writer.writerow([r['country'], round(r['lambda'], 4), round(r['sigma_index'], 2)])

print("\n✅ Đã xuất file: LAMBDA_FINAL_REPORT.csv")
