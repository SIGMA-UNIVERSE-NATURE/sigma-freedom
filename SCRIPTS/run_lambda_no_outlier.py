#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import math

WEIGHTS = {
    'flood': 0.30, 'typhoon': 0.15, 'hurricane': 0.15,
    'earthquake': 0.12, 'wildfire': 0.08, 'drought': 0.05,
    'landslide': 0.10, 'tornado': 0.02, 'heatwave': 0.03,
    'winter_storm': 0.03, 'tsunami': 0.03
}

print("\n📂 Đang đọc dữ liệu...")
with open('DATA/PARAMETERS/lambda_global.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

regions = data.get('regions', {})
results = []

for country, hazards in regions.items():
    if country in ['sea', 'europe']:
        continue

    total = 0
    total_w = 0
    for hazard, value in hazards.items():
        if isinstance(value, dict) and 'lambda' in value:
            raw = value['lambda']
            if isinstance(raw, (int, float)) and raw > 0:
                log_val = math.log(raw + 1)
                w = WEIGHTS.get(hazard, 0.10)
                total += log_val * w
                total_w += w

    score = total / total_w if total_w > 0 else 0
    results.append((country, score))

# Loại bỏ Mỹ khỏi chuẩn hóa
filtered = [r for r in results if r[0] != 'us']
scores = [r[1] for r in filtered]
min_s = min(scores)
max_s = max(scores)

# Chuẩn hóa cho tất cả các nước (trừ Mỹ)
normalized = []
for country, score in results:
    if country == 'us':
        # Gán mức cao nhất hợp lý
        normalized.append((country, 98.0))
    else:
        val = ((score - min_s) / (max_s - min_s)) * 100
        normalized.append((country, val))

normalized.sort(key=lambda x: x[1], reverse=True)

print("\n" + "="*80)
print("       🌍 CHỈ SỐ RỦI RO THIÊN TAI SIGMA (LOẠI BỎ NGOẠI LỆ)       ")
print("="*80)
print(f"{'Quốc gia':<15} | {'SIGMA Index':<13}")
print("-"*40)
for country, val in normalized:
    print(f"{country:<15} | {val:<13.2f}")
print("="*80)

with open('LAMBDA_NO_OUTLIER.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Country', 'SIGMA_Index'])
    for country, val in normalized:
        writer.writerow([country, round(val, 2)])

print("\n✅ Đã xuất file: LAMBDA_NO_OUTLIER.csv")
