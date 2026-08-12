#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import math

WEIGHTS = {
    'flood': 0.25, 'typhoon': 0.22, 'hurricane': 0.22,
    'earthquake': 0.18, 'wildfire': 0.08, 'drought': 0.08,
    'landslide': 0.10, 'tornado': 0.03, 'heatwave': 0.05,
    'winter_storm': 0.02, 'tsunami': 0.07
}

REGION_WEIGHTS = {
    'sea': 1.6,    # Đông Nam Á
    'sa': 1.5,     # Nam Á
    'af': 1.3,     # Châu Phi
    'eu': 0.7,     # Châu Âu
    'na': 1.0,     # Bắc Mỹ
    'sa_am': 1.4   # Nam Mỹ
}

REGION_MAP = {
    'vietnam': 'sea', 'philippines': 'sea', 'indonesia': 'sea', 'thailand': 'sea',
    'india': 'sa', 'pakistan': 'sa', 'bangladesh': 'sa',
    'kenya': 'af', 'ethiopia': 'af', 'nigeria': 'af', 'south_africa': 'af',
    'us': 'na', 'canada': 'na', 'mexico': 'na',
    'peru': 'sa_am', 'colombia': 'sa_am', 'brazil': 'sa_am', 'argentina': 'sa_am', 'chile': 'sa_am',
    'uk': 'eu', 'germany': 'eu', 'france': 'eu', 'italy': 'eu', 'spain': 'eu', 'greece': 'eu',
    'japan': 'sea', 'taiwan': 'sea', 'south_korea': 'sea',
    'turkey': 'eu', 'iran': 'sa', 'china': 'sea', 'australia': 'sa_am', 'new_zealand': 'sa_am'
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

    for hazard, value in hazards.items():
        if isinstance(value, dict) and 'lambda' in value:
            raw = value['lambda']
            if isinstance(raw, (int, float)) and raw > 0:
                log_val = math.log(raw + 1)
                weight = WEIGHTS.get(hazard, 0.10)
                total_weighted += log_val * weight
                total_weight += weight

    avg_log = total_weighted / total_weight if total_weight > 0 else 0
    region = REGION_MAP.get(country, 'eu')
    region_weight = REGION_WEIGHTS.get(region, 1.0)
    adjusted_score = avg_log * region_weight

    results.append({
        'country': country,
        'raw_log': avg_log,
        'adjusted_score': adjusted_score,
        'region': region,
        'region_weight': region_weight
    })

# Chuẩn hóa Min-Max
scores = [r['adjusted_score'] for r in results]
min_val = min(scores)
max_val = max(scores)
range_val = max_val - min_val

if range_val > 0:
    for r in results:
        r['sigma_index'] = ((r['adjusted_score'] - min_val) / range_val) * 100
else:
    for r in results:
        r['sigma_index'] = 0

results.sort(key=lambda x: x['sigma_index'], reverse=True)

print("\n" + "="*80)
print("       🌍 CHỈ SỐ RỦI RO THIÊN TAI SIGMA (CHUẨN HÓA VÙNG)       ")
print("="*80)
print(f"{'Quốc gia':<15} | {'Vùng':<6} | {'Hệ số':<8} | {'SIGMA Index':<13}")
print("-"*70)

for r in results:
    print(f"{r['country']:<15} | {r['region']:<6} | {r['region_weight']:<8.2f} | {r['sigma_index']:<13.2f}")

print("="*80)

with open('LAMBDA_REGION_SCALED.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Country', 'Region', 'Region_Weight', 'SIGMA_Index'])
    for r in results:
        writer.writerow([r['country'], r['region'], r['region_weight'], round(r['sigma_index'], 2)])

print("\n✅ Đã xuất file: LAMBDA_REGION_SCALED.csv")
