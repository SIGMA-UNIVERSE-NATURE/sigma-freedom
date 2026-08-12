



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
run_lambda_corrected.py
Tính toán λ tổng hợp với log-transform và chuẩn hóa nội bộ
"""

import json
import csv
import math

# ====== TRỌNG SỐ ======
WEIGHTS = {
    'flood': 0.20, 'typhoon': 0.18, 'hurricane': 0.18,
    'earthquake': 0.15, 'wildfire': 0.12, 'drought': 0.10,
    'landslide': 0.08, 'tornado': 0.05, 'heatwave': 0.05,
    'winter_storm': 0.04, 'tsunami': 0.03
}
DEFAULT_WEIGHT = 0.10

# ====== ĐỌC DỮ LIỆU ======
print("\n📂 Đang đọc dữ liệu...")
with open('DATA/PARAMETERS/lambda_global.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

regions = data.get('regions', {})
results = []

for country, hazards in regions.items():
    if country in ['sea', 'europe']:
        continue

    total_log = 0
    total_weight = 0

    for hazard, value in hazards.items():
        if isinstance(value, dict) and 'lambda' in value:
            raw = value['lambda']
            if isinstance(raw, (int, float)) and raw > 0:
                # Log-transform để thu nhỏ giá trị lớn
                log_val = math.log(raw + 1)
                weight = WEIGHTS.get(hazard, DEFAULT_WEIGHT)
                total_log += log_val * weight
                total_weight += weight

    avg_log = total_log / total_weight if total_weight > 0 else 0
    results.append({'country': country, 'log_lambda': avg_log})

# ====== CHUẨN HÓA VỀ THANG 0-100 BẰNG CÁCH KHẮC PHỤC NGOẠI LỆ ======
log_vals = [r['log_lambda'] for r in results]

# Loại bỏ ngoại lệ (outlier) nếu có
log_vals_sorted = sorted(log_vals)
q1 = log_vals_sorted[int(len(log_vals_sorted) * 0.25)]
q3 = log_vals_sorted[int(len(log_vals_sorted) * 0.75)]
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Lọc các giá trị nằm trong khoảng hợp lý
filtered_vals = [v for v in log_vals if lower_bound <= v <= upper_bound]

if filtered_vals:
    min_val = min(filtered_vals)
    max_val = max(filtered_vals)
else:
    min_val = min(log_vals)
    max_val = max(log_vals)

range_val = max_val - min_val

if range_val > 0:
    for r in results:
        # Chuẩn hóa nhưng giới hạn trong khoảng 0-100
        raw_score = ((r['log_lambda'] - min_val) / range_val) * 100
        r['sigma_index'] = max(0, min(100, raw_score))  # Giới hạn 0-100
else:
    for r in results:
        r['sigma_index'] = 0

# Sắp xếp giảm dần
results.sort(key=lambda x: x['sigma_index'], reverse=True)

# ====== XUẤT KẾT QUẢ ======
print("\n" + "="*80)
print("       🌍 CHỈ SỐ RỦI RO THIÊN TAI SIGMA (LOG-TRANSFORM)       ")
print("="*80)
print(f"{'Quốc gia':<15} | {'log λ':<12} | {'SIGMA Index':<13}")
print("-"*60)

for r in results:
    print(f"{r['country']:<15} | {r['log_lambda']:<12.4f} | {r['sigma_index']:<13.2f}")

print("="*80)

# ====== LƯU FILE ======
with open('LAMBDA_CORRECTED_REPORT.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Country', 'Log_Lambda', 'SIGMA_Index'])
    for r in results:
        writer.writerow([r['country'], round(r['log_lambda'], 4), round(r['sigma_index'], 2)])

print("\n✅ Đã xuất file: LAMBDA_CORRECTED_REPORT.csv")
