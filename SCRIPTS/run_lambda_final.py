#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
run_lambda_final.py
Tính toán SIGMA Index với chuẩn hóa nội bộ từng loại thiên tai
"""

import json
import csv
import math

WEIGHTS = {
    'flood': 0.20, 'typhoon': 0.18, 'hurricane': 0.18,
    'earthquake': 0.15, 'wildfire': 0.12, 'drought': 0.10,
    'landslide': 0.08, 'tornado': 0.05, 'heatwave': 0.05,
    'winter_storm': 0.04, 'tsunami': 0.03
}
DEFAULT_WEIGHT = 0.10

print("\n📂 Đang đọc dữ liệu...")
with open('DATA/PARAMETERS/lambda_global.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

regions = data.get('regions', {})
all_hazards = {}

# Thu thập tất cả giá trị lambda theo từng loại thiên tai
for country, hazards in regions.items():
    if country in ['sea', 'europe']:
        continue
    for hazard, value in hazards.items():
        if isinstance(value, dict) and 'lambda' in value:
            raw = value['lambda']
            if isinstance(raw, (int, float)) and raw > 0:
                all_hazards.setdefault(hazard, []).append(raw)

# Tính log trung bình cho từng loại
hazard_log_avg = {}
for hazard, values in all_hazards.items():
    hazard_log_avg[hazard] = sum([math.log(v + 1) for v in values]) / len(values)

# Tính điểm cho từng quốc gia
results = []
for country, hazards in regions.items():
    if country in ['sea', 'europe']:
        continue

    total_score = 0
    total_weight = 0

    for hazard, value in hazards.items():
        if isinstance(value, dict) and 'lambda' in value:
            raw = value['lambda']
            if isinstance(raw, (int, float)) and raw > 0:
                log_val = math.log(raw + 1)
                avg_log = hazard_log_avg.get(hazard, 1)
                # Điểm tương đối so với trung bình thế giới
                relative_score = log_val / avg_log if avg_log > 0 else 1
                weight = WEIGHTS.get(hazard, DEFAULT_WEIGHT)
                total_score += relative_score * weight
                total_weight += weight

    final_score = total_score / total_weight if total_weight > 0 else 0
    results.append({'country': country, 'relative_score': final_score})

# Chuẩn hóa từ 0-100
scores = [r['relative_score'] for r in results]
min_val = min(scores)
max_val = max(scores)
range_val = max_val - min_val

if range_val > 0:
    for r in results:
        r['sigma_index'] = ((r['relative_score'] - min_val) / range_val) * 100
else:
    for r in results:
        r['sigma_index'] = 0

results.sort(key=lambda x: x['sigma_index'], reverse=True)

print("\n" + "="*80)
print("       🌍 CHỈ SỐ RỦI RO THIÊN TAI SIGMA (CHUẨN HÓA NỘI BỘ)       ")
print("="*80)
print(f"{'Quốc gia':<15} | {'Điểm tương đối':<15} | {'SIGMA Index':<13}")
print("-"*65)

for r in results:
    print(f"{r['country']:<15} | {r['relative_score']:<15.4f} | {r['sigma_index']:<13.2f}")

print("="*80)

with open('LAMBDA_FINAL_REPORT.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Country', 'Relative_Score', 'SIGMA_Index'])
    for r in results:
        writer.writerow([r['country'], round(r['relative_score'], 4), round(r['sigma_index'], 2)])

print("\n✅ Đã xuất file: LAMBDA_FINAL_REPORT.csv")
