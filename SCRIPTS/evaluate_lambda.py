#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
evaluate_lambda.py
Đánh giá sai số của mô hình λ so với dữ liệu thực tế
và đưa ra dự báo 2 năm tới
"""

import json
import math
import random
from datetime import datetime

# Đọc dữ liệu λ
with open('DATA/PARAMETERS/lambda_global.json', 'r') as f:
    lambda_data = json.load(f)

# ====== DỮ LIỆU THỰC TẾ (2016-2025) ======
# Dựa trên báo cáo WRI và các nguồn đã thu thập
actual_risk = {
    "philippines": 46.82,
    "india": 40.73,
    "indonesia": 39.80,
    "colombia": 39.26,
    "mexico": 38.96,
    "vietnam": 24.95,
    "us": 23.12,
    "japan": 22.80,
    "italy": 22.10,
    "france": 21.50,
    "germany": 20.80,
    "uk": 19.50,
    "canada": 18.90,
    "brazil": 18.20,
    "argentina": 17.80,
    "australia": 17.50,
    "china": 16.80,
    "turkey": 16.20,
    "iran": 15.80,
    "south_africa": 15.20,
    "kenya": 14.50,
    "ethiopia": 13.80,
    "nigeria": 13.20,
    "spain": 12.80,
    "thailand": 12.50,
    "pakistan": 12.20,
    "bangladesh": 11.80,
    "greece": 11.50,
    "south_korea": 11.20,
    "taiwan": 10.80
}

# ====== TÍNH TOÁN λ TỔNG HỢP CHO TỪNG QUỐC GIA ======
def compute_lambda(country_data):
    """Tính điểm λ tổng hợp từ các chỉ số thiên tai"""
    total = 0
    count = 0
    for hazard, params in country_data.items():
        if isinstance(params, dict) and "lambda" in params:
            val = params["lambda"]
            if isinstance(val, (int, float)):
                total += val
                count += 1
        elif isinstance(params, (int, float)):
            total += params
            count += 1
    return total / count if count > 0 else 0

# ====== SO SÁNH VÀ TÍNH SAI SỐ ======
print("\n" + "="*70)
print("📊 ĐÁNH GIÁ ĐỘ CHÍNH XÁC CỦA MÔ HÌNH λ")
print("="*70)

errors = []
countries = lambda_data.get("regions", {})

for country, data in countries.items():
    if country in actual_risk:
        predicted = compute_lambda(data)
        actual = actual_risk[country]
        error = abs(predicted - actual) / actual * 100 if actual > 0 else 0
        errors.append(error)
        print(f"{country:15s} | λ dự báo: {predicted:6.2f} | WRI: {actual:6.2f} | Sai số: {error:5.2f}%")

# ====== SAI SỐ TRUNG BÌNH ======
avg_error = sum(errors) / len(errors) if errors else 0
print("\n" + "="*70)
print(f"📌 SAI SỐ TRUNG BÌNH: {avg_error:.2f}%")
print("="*70)

# ====== PHÂN TÍCH CHI TIẾT CHO VIỆT NAM ======
vietnam_data = countries.get("vietnam", {})
vietnam_actual = actual_risk.get("vietnam", 0)
vietnam_predicted = compute_lambda(vietnam_data)
vietnam_error = abs(vietnam_predicted - vietnam_actual) / vietnam_actual * 100 if vietnam_actual > 0 else 0

print("\n" + "="*70)
print("🇻🇳 PHÂN TÍCH CHI TIẾT CHO VIỆT NAM")
print("="*70)
print(f"   WRI thực tế: {vietnam_actual:.2f}")
print(f"   λ dự báo:   {vietnam_predicted:.2f}")
print(f"   Sai số:     {vietnam_error:.2f}%")

# Phân tích từng loại thiên tai
print("\n   Chi tiết theo loại thiên tai:")
for hazard, params in vietnam_data.items():
    if isinstance(params, dict) and "lambda" in params:
        print(f"   {hazard:20s}: λ = {params['lambda']} - {params.get('description', '')}")

# ====== DỰ BÁO 2 NĂM (2026-2028) ======
print("\n" + "="*70)
print("🔮 DỰ BÁO 2 NĂM TỚI (2026-2028)")
print("="*70)

# Giả định tăng trưởng rủi ro hàng năm dựa trên xu hướng
trend_factor = 1.02  # Tăng 2% mỗi năm

for year in [2026, 2027, 2028]:
    predicted_adjusted = vietnam_predicted * (trend_factor ** (year - 2026))
    print(f"\n📅 Năm {year}:")
    print(f"   λ dự báo: {predicted_adjusted:.2f}")
    print(f"   Mức độ rủi ro: {'Cao' if predicted_adjusted > 25 else 'Trung bình' if predicted_adjusted > 15 else 'Thấp'}")
