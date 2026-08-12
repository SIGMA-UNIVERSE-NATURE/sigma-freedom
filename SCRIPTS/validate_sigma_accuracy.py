#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
validate_sigma_accuracy.py
Kiểm tra độ chính xác của SIGMA Index so với dữ liệu thực tế
"""

import csv
import math

# ====== DỮ LIỆU THỰC TẾ (THAM KHẢO) ======
# Điểm tham khảo dựa trên WRI và các báo cáo quốc tế
reference_data = {
    'us': 23.12,
    'japan': 21.00,
    'india': 40.73,
    'vietnam': 24.95,
    'philippines': 46.82,
    'indonesia': 39.80,
    'mexico': 38.96,
    'brazil': 17.50,
    'colombia': 39.26,
    'argentina': 18.00,
    'chile': 22.00,
    'peru': 32.00,
    'turkey': 25.00,
    'iran': 21.00,
    'south_africa': 16.00,
    'kenya': 28.00,
    'ethiopia': 26.06,
    'nigeria': 31.00,
    'spain': 14.42,
    'italy': 13.67,
    'germany': 1.60,
    'france': 29.33,
    'uk': 5.00,
    'canada': 12.00,
    'new_zealand': 17.05,
    'thailand': 9.79,
    'pakistan': 38.50,
    'bangladesh': 59.31,
    'greece': 1.19,
    'south_korea': 6.13,
    'taiwan': 11.95
}

# Đọc file CSV đã xuất
print("\n📂 Đang đọc dữ liệu SIGMA Index từ LAMBDA_UPDATED_REPORT.csv...")
sigma_data = {}

try:
    with open('LAMBDA_UPDATED_REPORT.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country = row['Country']
            sigma_index = float(row['SIGMA_Index'])
            sigma_data[country] = sigma_index
except FileNotFoundError:
    print("❌ Không tìm thấy file LAMBDA_UPDATED_REPORT.csv")
    exit(1)

# ====== SO SÁNH VÀ ĐÁNH GIÁ ======
print("\n" + "="*80)
print("       📊 KIỂM TRA ĐỘ CHÍNH XÁC CỦA SIGMA INDEX       ")
print("="*80)

total_countries = 0
accurate_countries = 0
error_list = []

for country, sigma_val in sigma_data.items():
    if country in reference_data:
        total_countries += 1
        ref_val = reference_data[country]
        # Cho phép sai số ±10%
        error_percent = abs(sigma_val - ref_val) / ref_val * 100 if ref_val > 0 else 0
        is_accurate = error_percent <= 10.0

        if is_accurate:
            accurate_countries += 1

        error_list.append({
            'country': country,
            'sigma': sigma_val,
            'reference': ref_val,
            'error': error_percent,
            'accurate': is_accurate
        })

# Sắp xếp theo độ sai số giảm dần
error_list.sort(key=lambda x: x['error'], reverse=True)

# Hiển thị kết quả
print(f"\n{'Quốc gia':<15} | {'SIGMA':<8} | {'Tham chiếu':<10} | {'Sai số %':<10} | {'Kết quả':<10}")
print("-"*70)

for item in error_list:
    result = "✅ Đạt" if item['accurate'] else "❌ Chưa đạt"
    print(f"{item['country']:<15} | {item['sigma']:<8.2f} | {item['reference']:<10.2f} | {item['error']:<10.2f} | {result:<10}")

# ====== TỔNG KẾT ======
accuracy_rate = (accurate_countries / total_countries) * 100 if total_countries > 0 else 0

print("\n" + "="*80)
print(f"📌 TỔNG KẾT:")
print(f"   Tổng số quốc gia có dữ liệu tham chiếu: {total_countries}")
print(f"   Số quốc gia đạt độ chính xác (sai số ≤ 10%): {accurate_countries}")
print(f"   Tỷ lệ chính xác: {accuracy_rate:.2f}%")
print("="*80)

if accuracy_rate >= 70:
    print("\n🎯 KẾT LUẬN: Mô hình SIGMA Index đạt độ chính xác ≥ 70%. Có thể công bố!")
else:
    print("\n⚠️ KẾT LUẬN: Mô hình chưa đạt độ chính xác 70%. Cần điều chỉnh thêm.")
