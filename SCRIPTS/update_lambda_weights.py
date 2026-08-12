#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
update_lambda_weights.py
Cập nhật trọng số và hệ số vùng dựa trên thực tế
"""

import json
import csv
import math

# Cập nhật trọng số cho từng loại thiên tai
WEIGHTS = {
    'flood': 0.25,
    'typhoon': 0.22,
    'hurricane': 0.22,
    'earthquake': 0.18,
    'wildfire': 0.08,
    'drought': 0.08,
    'landslide': 0.10,
    'tornado': 0.03,
    'heatwave': 0.05,
    'winter_storm': 0.02,
    'tsunami': 0.07
}
DEFAULT_WEIGHT = 0.10

# Cập nhật hệ số vùng dựa trên thực tế
REGION_FACTORS = {
    'us': 1.0,
    'japan': 1.3,
    'philippines': 1.5,
    'vietnam': 1.4,
    'indonesia': 1.5,
    'bangladesh': 1.6,
    'india': 1.2,
    'china': 1.1,
    'uk': 0.6,
    'germany': 0.4,
    'peru': 1.3,
    'colombia': 1.3,
    'mexico': 1.2,
    'turkey': 1.1,
    'iran': 1.0,
    'pakistan': 1.2,
    'thailand': 1.1,
    'taiwan': 1.2,
    'south_korea': 1.0,
    'australia': 0.8,
    'canada': 0.7,
    'france': 0.7,
    'italy': 0.8,
    'spain': 0.7,
    'greece': 0.6,
    'brazil': 0.7,
    'argentina': 0.6,
    'chile': 0.8,
    'south_africa': 0.6,
    'kenya': 0.7,
    'ethiopia': 0.6,
    'nigeria': 0.5,
    'new_zealand': 0.9
}

print("\n📂 Đang đọc dữ liệu...")
with open('DATA/PARAMETERS/lambda_global.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

regions = data.get('regions', {})
results = []

for country, hazards in regions.items():
    if country in ['sea', 'europe']:
        continue

    total_weighted = 0
    total_weight = 0
    hazard_count = 0

    for hazard, value in hazards.items():
        if isinstance(value, dict) and 'lambda' in value:
            raw = value['lambda']
            if isinstance(raw, (int, float)) and raw > 0:
                log_val = math.log(raw + 1)
                weight = WEIGHTS.get(hazard, DEFAULT_WEIGHT)
                total_weighted += log_val * weight
                total_weight += weight
                hazard_count += 1

    avg_log = total_weighted / total_weight if total_weight > 0 else 0
    factor = REGION_FACTORS.get(country, 1.0)
    adjusted_score = avg_log * factor

    results.append({
        'country': country,
        'raw_log': avg_log,
        'adjusted_score': adjusted_score,
        'factor': factor,
        'hazard_count': hazard_count
    })

# Chuẩn hóa về thang 0-100
scores = [r['adjusted_score'] for r in results]
min_val = min(scores)
max_val = max(scores)
range_val = max_val - min_val

if range_val > 0:
    for r in results:
        raw_score = ((r['adjusted_score'] - min_val) / range_val) * 100
        r['sigma_index'] = max(0, min(100, raw_score))
else:
    for r in results:
        r['sigma_index'] = 0

results.sort(key=lambda x: x['sigma_index'], reverse=True)

# Xuất kết quả
print("\n" + "="*80)
print("       🌍 CHỈ SỐ RỦI RO THIÊN TAI SIGMA (CẬP NHẬT)       ")
print("="*80)
print(f"{'Quốc gia':<15} | {'log λ':<10} | {'Hệ số':<8} | {'Số loại':<8} | {'SIGMA Index':<13}")
print("-"*75)

for r in results:
    print(f"{r['country']:<15} | {r['raw_log']:<10.4f} | {r['factor']:<8.2f} | {r['hazard_count']:<8} | {r['sigma_index']:<13.2f}")

print("="*80)

# Lưu file CSV
with open('LAMBDA_UPDATED_REPORT.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Country', 'Raw_Log', 'Factor', 'Hazard_Count', 'SIGMA_Index'])
    for r in results:
        writer.writerow([r['country'], round(r['raw_log'], 4), round(r['factor'], 2), r['hazard_count'], round(r['sigma_index'], 2)])

print("\n✅ Đã xuất file: LAMBDA_UPDATED_REPORT.csv")
