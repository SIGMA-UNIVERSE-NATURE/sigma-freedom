#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime

# ====== DỮ LIỆU LAMBDA CHO CÁC KHU VỰC ======
lambda_global = {
    "last_updated": datetime.now().isoformat(),
    "regions": {
        "us": {
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
        },
        "sea": {
            "earthquake": {
                "M4.5": 28.0,
                "M5.0": 8.0,
                "M5.5": 2.5,
                "M6.0": 0.8
            },
            "typhoon": {
                "lambda": 25,
                "seasonal_peak": [9, 10, 11]
            },
            "flood": {
                "mekong": {
                    "low": 0.5,
                    "medium": 1.2,
                    "high": 2.5
                }
            }
        },
        "japan": {
            "earthquake": {
                "M4.5": 15.0,
                "M5.0": 4.5,
                "M5.5": 1.2,
                "M6.0": 0.4
            }
        },
        "europe": {
            "flood": {
                "lambda": 0.8
            },
            "wildfire": {
                "lambda": 1500
            }
        }
    }
}

# ====== LƯU FILE ======
os.makedirs("DATA/PARAMETERS", exist_ok=True)
with open("DATA/PARAMETERS/lambda_global.json", "w") as f:
    json.dump(lambda_global, f, indent=4)

print("✅ Đã tạo bảng λ toàn cầu tại DATA/PARAMETERS/lambda_global.json")
print("📊 Các khu vực:", ", ".join(lambda_global["regions"].keys()))
