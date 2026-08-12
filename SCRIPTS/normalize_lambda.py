#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
normalize_lambda.py
Chuẩn hóa λ về thang điểm 0-100 để so sánh với WRI
"""

import json

# Đọc dữ liệu
with open('DATA/PARAMETERS/lambda_global.json', 'r') as f:
    data = json.load(f)

regions = data.get('regions', {})

# Xác định giá trị λ tối đa cho từng loại thiên tai
max_values = {}
for country, hazards in regions.items():
    for hazard, params in hazards.items():
        if isinstance(params, dict) and 'lambda' in params:
            val = params['lambda']
            if isinstance(val, (int, float)):
                if hazard not in max_values or val > max_values[hazard]:
                    max_values[hazard] = val

print("="*70)
print("📊 CHUẨN HÓA λ VỀ THANG ĐIỂM 0-100")
print("="*70)

# Chuẩn hóa và tính toán lại
normalized_data = {}
for country, hazards in regions.items():
    normalized_data[country] = {}
    total_normalized = 0
    count = 0
    for hazard, params in hazards.items():
        if isinstance(params, dict) and 'lambda' in params:
            val = params['lambda']
            if isinstance(val, (int, float)) and hazard in max_values:
                max_val = max_values[hazard]
                norm = (val / max_val) * 100 if max_val > 0 else 0
                normalized_data[country][hazard] = round(norm, 2)
                total_normalized += norm
                count += 1
    if count > 0:
        normalized_data[country]['avg'] = round(total_normalized / count, 2)

# In kết quả
for country, hazards in normalized_data.items():
    avg = hazards.get('avg', 0)
    print(f"{country:15s} | λ chuẩn hóa: {avg:6.2f} (0-100)")
