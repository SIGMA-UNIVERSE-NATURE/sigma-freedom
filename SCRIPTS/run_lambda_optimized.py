#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import math
import itertools

WEIGHTS_CANDIDATES = {
    'flood': [0.20, 0.25, 0.30],
    'typhoon': [0.15, 0.20, 0.25],
    'hurricane': [0.15, 0.20, 0.25],
    'earthquake': [0.12, 0.15, 0.18],
    'wildfire': [0.05, 0.08, 0.12],
    'drought': [0.05, 0.08, 0.10],
    'landslide': [0.06, 0.08, 0.10],
    'tornado': [0.02, 0.03, 0.05],
    'heatwave': [0.03, 0.05, 0.07],
    'winter_storm': [0.01, 0.02, 0.03],
    'tsunami': [0.03, 0.05, 0.07]
}

REFERENCE = {
    'us': 23.12, 'japan': 21.00, 'india': 40.73, 'vietnam': 24.95,
    'philippines': 46.82, 'indonesia': 39.80, 'mexico': 38.96,
    'brazil': 17.50, 'colombia': 39.26, 'argentina': 18.00,
    'chile': 22.00, 'peru': 32.00, 'turkey': 25.00, 'iran': 21.00,
    'south_africa': 16.00, 'kenya': 28.00, 'ethiopia': 26.06,
    'nigeria': 31.00, 'spain': 14.42, 'italy': 13.67,
    'germany': 1.60, 'france': 29.33, 'uk': 5.00, 'canada': 12.00,
    'new_zealand': 17.05, 'thailand': 9.79, 'pakistan': 38.50,
    'bangladesh': 59.31, 'greece': 1.19, 'south_korea': 6.13, 'taiwan': 11.95
}

print("\n📂 Đang đọc dữ liệu...")
with open('DATA/PARAMETERS/lambda_global.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

regions = data.get('regions', {})
country_hazards = {}

for country, hazards in regions.items():
    if country in ['sea', 'europe']:
        continue
    country_hazards[country] = {}
    for hazard, value in hazards.items():
        if isinstance(value, dict) and 'lambda' in value:
            raw = value['lambda']
            if isinstance(raw, (int, float)) and raw > 0:
                country_hazards[country][hazard] = math.log(raw + 1)

print(f"✅ Đã tải dữ liệu cho {len(country_hazards)} quốc gia.")

# Chuẩn bị các tổ hợp trọng số
keys = list(WEIGHTS_CANDIDATES.keys())
combinations = list(itertools.product(*[WEIGHTS_CANDIDATES[k] for k in keys]))

print(f"🔄 Đang thử nghiệm {len(combinations)} tổ hợp trọng số...")

best_weights = None
best_score = float('inf')

for combo in combinations:
    weights = dict(zip(keys, combo))
    results = []

    for country, hazards in country_hazards.items():
        total = 0
        total_w = 0
        for hazard, log_val in hazards.items():
            w = weights.get(hazard, 0.10)
            total += log_val * w
            total_w += w
        score = total / total_w if total_w > 0 else 0
        results.append((country, score))

    scores = [r[1] for r in results]
    min_s = min(scores)
    max_s = max(scores)
    if max_s > min_s:
        normalized = [(c, ((s - min_s) / (max_s - min_s)) * 100) for c, s in results]
    else:
        normalized = [(c, 0) for c, s in results]

    errors = []
    for country, val in normalized:
        if country in REFERENCE:
            ref = REFERENCE[country]
            if ref > 0:
                errors.append(abs(val - ref) / ref)
    if errors:
        avg_error = sum(errors) / len(errors)
        if avg_error < best_score:
            best_score = avg_error
            best_weights = weights

print("\n✅ Tìm thấy bộ trọng số tối ưu!")
print("📊 Trọng số tối ưu:")
for k, v in best_weights.items():
    print(f"   {k}: {v:.2f}")

# Tái tính với bộ trọng số tối ưu
results = []
for country, hazards in country_hazards.items():
    total = 0
    total_w = 0
    for hazard, log_val in hazards.items():
        w = best_weights.get(hazard, 0.10)
        total += log_val * w
        total_w += w
    score = total / total_w if total_w > 0 else 0
    results.append((country, score))

scores = [r[1] for r in results]
min_s = min(scores)
max_s = max(scores)
if max_s > min_s:
    normalized = [(c, ((s - min_s) / (max_s - min_s)) * 100) for c, s in results]
else:
    normalized = [(c, 0) for c, s in results]

normalized.sort(key=lambda x: x[1], reverse=True)

print("\n" + "="*80)
print("       🌍 CHỈ SỐ RỦI RO THIÊN TAI SIGMA (TỐI ƯU HÓA TOÀN DIỆN)       ")
print("="*80)
print(f"{'Quốc gia':<15} | {'SIGMA Index':<13}")
print("-"*40)
for country, val in normalized:
    print(f"{country:<15} | {val:<13.2f}")
print("="*80)

with open('LAMBDA_OPTIMIZED.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Country', 'SIGMA_Index'])
    for country, val in normalized:
        writer.writerow([country, round(val, 2)])
