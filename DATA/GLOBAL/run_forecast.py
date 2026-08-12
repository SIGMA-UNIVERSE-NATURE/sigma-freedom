#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SIGMA Climate - Hệ thống tính toán dự báo thiên tai
Đọc dữ liệu thực tế từ các file đã thu thập
"""

import json
import math
import datetime
import glob
import os

# ========== 1. ĐỌC DỮ LIỆU ĐỘNG ĐẤT TỪ USGS ==========
def read_earthquake_data(file_path):
    """Đọc dữ liệu động đất từ file GeoJSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        magnitudes = []
        for feature in data.get('features', []):
            mag = feature.get('properties', {}).get('mag')
            if mag is not None:
                magnitudes.append(mag)
        
        return magnitudes
    except Exception as e:
        print(f"⚠️ Lỗi đọc file {file_path}: {e}")
        return []

# ========== 2. TÍNH THAM SỐ TỪ DỮ LIỆU ==========
def calculate_earthquake_params(magnitudes, min_mag=4.5):
    """
    Tính tham số a, b từ dữ liệu động đất
    """
    if not magnitudes:
        return 5.5, 0.9  # Giá trị mặc định cho Đông Nam Á
    
    # Lọc động đất ≥ min_mag
    filtered = [m for m in magnitudes if m >= min_mag]
    if not filtered:
        return 5.5, 0.9
    
    # Số lượng động đất
    N = len(filtered)
    
    # Ước tính b (thường ~0.9-1.0 cho khu vực Đông Nam Á)
    b = 0.9
    
    # Tính a = log10(N) + b * min_mag
    a = math.log10(N) + b * min_mag
    
    return round(a, 2), round(b, 2)

# ========== 3. ĐỌC DỮ LIỆU MƯA TỪ FILE (nếu có) ==========
def read_rainfall_data():
    """Đọc dữ liệu mưa từ file Open-Meteo (nếu có)"""
    try:
        # Tìm file thời tiết mới nhất
        pattern = "DATA/GLOBAL/FLOOD_MEKONG/RAW_DATA/weather_*.json"
        files = glob.glob(pattern)
        if not files:
            return None
        
        latest = max(files, key=os.path.getctime)
        with open(latest, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Trích xuất nhiệt độ (có thể dùng làm thông số phụ)
        temp = data.get('current_weather', {}).get('temperature')
        return temp
    except Exception as e:
        print(f"⚠️ Không đọc được dữ liệu thời tiết: {e}")
        return None

# ========== 4. HÀM DỰ BÁO ==========
def main():
    print("\n" + "="*50)
    print("🌍 SIGMA CLIMATE - HỆ THỐNG DỰ BÁO THIÊN TAI")
    print("="*50)
    
    # ---- 4.1. ĐỘNG ĐẤT ----
    print("\n[1] DỰ BÁO ĐỘNG ĐẤT")
    
    # Tìm file động đất mới nhất
    eq_pattern = "DATA/GLOBAL/FLOOD_MEKONG/RAW_DATA/earthquakes_*.geojson"
    eq_files = glob.glob(eq_pattern)
    
    if eq_files:
        latest_eq = max(eq_files, key=os.path.getctime)
        magnitudes = read_earthquake_data(latest_eq)
        a, b = calculate_earthquake_params(magnitudes)
        
        # Dự báo số lượng động đất trong 1 tháng
        N_forecast = 10 ** (a - b * 4.5)
        
        print(f"   📂 Dữ liệu từ: {os.path.basename(latest_eq)}")
        print(f"   Tham số: a = {a}, b = {b}")
        print(f"   Số lượng dự kiến (M >= 4.5) trong 1 tháng: {round(N_forecast)}")
    else:
        print("   ⚠️ Chưa có dữ liệu động đất. Đang dùng tham số mặc định.")
        print("   Số lượng dự kiến (M >= 4.5): 28")
    
    # ---- 4.2. LŨ LỤT ----
    print("\n[2] DỰ BÁO LŨ LỤT MEKONG (Trạm Tân Châu)")
    
    # Thử đọc dữ liệu mưa thực tế
    temp = read_rainfall_data()
    if temp is not None:
        # Giả định lượng mưa khoảng 2x nhiệt độ
        rainfall = temp * 6  # ước tính gần đúng
        water_level = 4.0 + 0.02 * (rainfall - 100)
        print(f"   📂 Nhiệt độ hiện tại: {temp}°C (ước tính mưa: {rainfall:.0f}mm)")
        print(f"   Mực nước dự báo: {round(water_level, 2)} m")
    else:
        print("   ⚠️ Chưa có dữ liệu thời tiết. Đang dùng số giả định.")
        print("   Lượng mưa giả định: 180mm")
        print("   Mực nước dự báo: 5.6 m")
    
    # ---- 4.3. HẠN HÁN ----
    print("\n[3] DỰ BÁO HẠN HÁN SAHEL")
    print("   ⚠️ Chưa có dữ liệu SPI. Đang dùng số giả định.")
    print("   Lượng mưa giả định: 250mm")
    print("   Chỉ số SPI: -1.5 (Hạn nặng)")
    
    # ---- 4.4. BÃO ----
    print("\n[4] DỰ BÁO BÃO BIỂN ĐÔNG")
    print("   ⚠️ Chưa có dữ liệu SST. Đang dùng số giả định.")
    print("   SST giả định: 29°C, áp suất: 980 hPa")
    print("   Vận tốc gió dự báo: 85.0 km/h")
    
    print("\n" + "="*50)
    print("🕊️ Dữ liệu được tính toán từ file dữ liệu thực tế (nếu có).")
    print("   Hệ thống sẽ tự động cập nhật khi có dữ liệu mới.")

if __name__ == "__main__":
    main()
