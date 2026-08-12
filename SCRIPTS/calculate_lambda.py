#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
calculate_lambda.py
Tính toán tham số λ từ bộ dữ liệu lambda_global.json
"""

import json
import os
from datetime import datetime

# Đường dẫn file
LAMBDA_FILE = "DATA/PARAMETERS/lambda_global.json"
OUTPUT_FILE = "DATA/PARAMETERS/lambda_computed.json"

# Đọc dữ liệu
try:
    with open(LAMBDA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("❌ Không tìm thấy file lambda_global.json")
    exit(1)
except json.JSONDecodeError as e:
    print(f"❌ Lỗi JSON: {e}")
    exit(1)

# Thêm thông tin thời gian tính toán
data["computed_at"] = datetime.now().isoformat()

# Tính toán thêm các chỉ số phụ (nếu cần)
regions = data.get("regions", {})
total_countries = len(regions)
total_hazards = 0

for country, hazards in regions.items():
    total_hazards += len(hazards)

data["summary"] = {
    "total_countries": total_countries,
    "total_hazards": total_hazards,
    "note": "Bộ tham số λ toàn cầu cho 38 quốc gia và 11 loại thiên tai"
}

# Lưu kết quả
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Đã tính toán và lưu kết quả vào {OUTPUT_FILE}")
print(f"   📊 Số quốc gia: {total_countries}")
print(f"   📋 Số loại thiên tai: {total_hazards}")
