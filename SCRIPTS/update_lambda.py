#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
update_lambda.py
Cập nhật tham số λ tự động từ dữ liệu mới nhất
SIGMA Climate - Very Sirius
"""

import json
import os
from datetime import datetime

# Đường dẫn lưu λ
LAMBDA_FILE = "DATA/PARAMETERS/lambda_us.json"

# Dữ liệu mẫu (sẽ được thay bằng dữ liệu thực tế khi có)
lambda_data = {
    "region": "US",
    "last_updated": datetime.now().isoformat(),
    "earthquake": {
        "M3.5": 27.02,
        "M4.0": 9.75,
        "M4.5": 3.05,
        "M5.0": 0.90,
        "M5.5": 0.22
    },
    "wildfire": {
        "lambda": 61500,
        "seasonal_peak": [7, 8, 9]
    },
    "flood": {
        "storm_high": 3.80,
        "storm_low": 2.40,
        "el_nino": 3.33,
        "normal": 3.00,
        "combined_high": 4.00
    }
}

# Lưu vào file JSON
os.makedirs(os.path.dirname(LAMBDA_FILE), exist_ok=True)
with open(LAMBDA_FILE, 'w') as f:
    json.dump(lambda_data, f, indent=4)

print(f"✅ Đã cập nhật λ cho Mỹ vào {LAMBDA_FILE}")
