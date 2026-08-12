#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SIGMA Climate - Hệ thống tính toán dự báo thiên tai
Dựa trên các công thức đã được xác định
"""

import json
import math
import datetime

# ========== 1. HÀM TÍNH TOÁN CHO ĐỘNG ĐẤT (Gutenberg-Richter) ==========
def earthquake_forecast(a=5.5, b=0.9, min_magnitude=4.5):
    """
    Tính số lượng động đất dự kiến có độ lớn >= min_magnitude
    """
    N = 10 ** (a - b * min_magnitude)
    return round(N)

# ========== 2. HÀM TÍNH TOÁN CHO LŨ LỤT (Tương quan mưa - mực nước) ==========
def flood_forecast(rainfall, avg_rainfall=100, avg_water_level=4.0, k=0.02):
    """
    Dự báo mực nước sông từ lượng mưa
    """
    water_level = avg_water_level + k * (rainfall - avg_rainfall)
    return round(water_level, 2)

# ========== 3. HÀM TÍNH TOÁN CHO HẠN HÁN (SPI) ==========
def drought_spi(rainfall, avg_rainfall=400, std_dev=100):
    """
    Tính chỉ số SPI từ lượng mưa
    """
    spi = (rainfall - avg_rainfall) / std_dev
    return round(spi, 2)

# ========== 4. HÀM TÍNH TOÁN CHO BÃO (Cường độ) ==========
def typhoon_intensity(sst, sst0=26.5, p_min=1000, p0=1000, alpha=10, beta=0.5, v0=50):
    """
    Dự báo vận tốc gió cực đại của bão
    """
    vmax = v0 + alpha * (sst - sst0) - beta * (p_min - p0)
    return round(vmax, 2)

# ========== 5. ĐỌC DỮ LIỆU ĐẦU VÀO (MÔ PHỎNG) ==========
def main():
    print("\n" + "="*50)
    print("🌍 SIGMA CLIMATE - HỆ THỐNG DỰ BÁO THIÊN TAI")
    print("="*50)
    print("\n[1] DỰ BÁO ĐỘNG ĐẤT")
    print("   Số lượng dự kiến (M >= 4.5):", earthquake_forecast())
    
    print("\n[2] DỰ BÁO LŨ LỤT MEKONG (Trạm Tân Châu)")
    print("   Lượng mưa giả định: 180mm")
    print("   Mực nước dự báo:", flood_forecast(180), "m")
    
    print("\n[3] DỰ BÁO HẠN HÁN SAHEL")
    print("   Lượng mưa giả định: 250mm")
    print("   Chỉ số SPI:", drought_spi(250))
    
    print("\n[4] DỰ BÁO BÃO BIỂN ĐÔNG")
    print("   SST giả định: 29°C, áp suất: 980 hPa")
    print("   Vận tốc gió dự báo:", typhoon_intensity(29, p_min=980), "km/h")
    
    print("\n" + "="*50)
    print("🕊️ Dữ liệu được tính toán dựa trên công thức và tham số chuẩn.")

if __name__ == "__main__":
    main()
