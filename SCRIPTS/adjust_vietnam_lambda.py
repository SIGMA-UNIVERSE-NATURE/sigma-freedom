#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
adjust_vietnam_lambda.py
Tự động điều chỉnh tham số λ cho Việt Nam
"""

import json
import os

# Đường dẫn file
LAMBDA_FILE = "DATA/PARAMETERS/lambda_global.json"
BACKUP_FILE = "DATA/PARAMETERS/lambda_global_backup.json"

# Đọc file JSON
with open(LAMBDA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Tạo bản sao lưu
with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Đã tạo bản sao lưu tại:", BACKUP_FILE)

# Điều chỉnh thông số cho Việt Nam
if "vietnam" in data["regions"]:
    vietnam = data["regions"]["vietnam"]
    
    # Cập nhật giá trị λ
    if "flood" in vietnam and isinstance(vietnam["flood"], dict):
        vietnam["flood"]["lambda"] = 4.5
        print("✅ Đã cập nhật flood.lambda = 4.5")
    
    if "wildfire" in vietnam and isinstance(vietnam["wildfire"], dict):
        vietnam["wildfire"]["lambda"] = 25
        print("✅ Đã cập nhật wildfire.lambda = 25")
    
    if "landslide" in vietnam and isinstance(vietnam["landslide"], dict):
        vietnam["landslide"]["lambda"] = 6.0
        print("✅ Đã cập nhật landslide.lambda = 6.0")
    
    # Lưu file
    with open(LAMBDA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("\n✅ Đã cập nhật thành công file lambda_global.json")
else:
    print("❌ Không tìm thấy dữ liệu cho Việt Nam")
