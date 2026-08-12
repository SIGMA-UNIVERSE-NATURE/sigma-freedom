#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
sigma_risk_model.py
Mô hình tính chỉ số rủi ro thiên tai SIGMA với hàm làm mượt sqrt
"""

import json
import math
import pandas as pd

# ====== DỮ LIỆU ĐẦU VÀO ======
raw_data = {
    "us": {"lambda": 83.33, "area": 9.83, "pop": 335.0, "wri": 23.12},
    "japan": {"lambda": 69.86, "area": 0.38, "pop": 124.0, "wri": 21.00},
    "india": {"lambda": 55.21, "area": 3.29, "pop": 1430.0, "wri": 40.73},
    "australia": {"lambda": 13.24, "area": 7.69, "pop": 26.5, "wri": 15.00},
    "china": {"lambda": 19.27, "area": 9.60, "pop": 1410.0, "wri": 16.50},
    "vietnam": {"lambda": 38.15, "area": 0.33, "pop": 100.0, "wri": 24.95},
    "philippines": {"lambda": 28.23, "area": 0.30, "pop": 117.0, "wri": 46.82},
    "indonesia": {"lambda": 61.64, "area": 1.91, "pop": 277.0, "wri": 39.80},
    "mexico": {"lambda": 12.25, "area": 1.96, "pop": 128.0, "wri": 38.96},
    "brazil": {"lambda": 8.51, "area": 8.51, "pop": 216.0, "wri": 17.50},
    "colombia": {"lambda": 51.26, "area": 1.14, "pop": 52.0, "wri": 39.26},
    "argentina": {"lambda": 22.88, "area": 2.78, "pop": 46.0, "wri": 18.00},
    "chile": {"lambda": 15.55, "area": 0.76, "pop": 19.6, "wri": 22.00},
    "peru": {"lambda": 45.55, "area": 1.29, "pop": 34.0, "wri": 32.00},
    "turkey": {"lambda": 8.82, "area": 0.78, "pop": 85.0, "wri": 25.00},
    "iran": {"lambda": 22.64, "area": 1.65, "pop": 89.0, "wri": 21.00},
    "south_africa": {"lambda": 10.99, "area": 1.22, "pop": 60.0, "wri": 16.00},
    "kenya": {"lambda": 20.66, "area": 0.58, "pop": 55.0, "wri": 28.00},
    "ethiopia": {"lambda": 26.06, "area": 1.10, "pop": 126.0, "wri": 26.06},
    "nigeria": {"lambda": 2.13, "area": 0.92, "pop": 224.0, "wri": 31.00},
    "spain": {"lambda": 14.42, "area": 0.51, "pop": 48.0, "wri": 14.42},
    "italy": {"lambda": 13.67, "area": 0.30, "pop": 59.0, "wri": 13.67},
    "germany": {"lambda": 1.60, "area": 0.36, "pop": 84.0, "wri": 1.60},
    "france": {"lambda": 29.33, "area": 0.55, "pop": 68.0, "wri": 29.33},
    "uk": {"lambda": 55.32, "area": 0.24, "pop": 67.0, "wri": 5.00},
    "canada": {"lambda": 34.04, "area": 9.98, "pop": 39.0, "wri": 12.00},
    "new_zealand": {"lambda": 17.05, "area": 0.27, "pop": 5.2, "wri": 17.05},
    "thailand": {"lambda": 9.79, "area": 0.51, "pop": 71.8, "wri": 9.79},
    "pakistan": {"lambda": 38.50, "area": 0.88, "pop": 240.0, "wri": 38.50},
    "bangladesh": {"lambda": 59.31, "area": 0.14, "pop": 173.0, "wri": 59.31},
    "greece": {"lambda": 1.19, "area": 0.13, "pop": 10.4, "wri": 1.19},
    "south_korea": {"lambda": 6.13, "area": 0.10, "pop": 51.7, "wri": 6.13},
    "taiwan": {"lambda": 11.95, "area": 0.04, "pop": 23.9, "wri": 11.95}
}

# ====== TÍNH TOÁN VỚI HÀM LÀM MƯỢT SQRT ======
rows = []
for country, data in raw_data.items():
    rows.append({
        "Country": country,
        "Raw_Lambda": data["lambda"],
        "Area": data["area"],
        "Pop": data["pop"],
        "WRI_2026": data["wri"],
        "Lambda_per_Area": data["lambda"] / math.sqrt(data["area"]),
        "Lambda_per_Pop": data["lambda"] / math.sqrt(data["pop"])
    })

df = pd.DataFrame(rows)

# ====== CHUẨN HÓA MIN-MAX ======
def min_max(series):
    return ((series - series.min()) / (series.max() - series.min())) * 100

df["Idx_Area_Scaled"] = min_max(df["Lambda_per_Area"])
df["Idx_Pop_Scaled"] = min_max(df["Lambda_per_Pop"])

# ====== CHỈ SỐ TỔNG HỢP (50/50) ======
df["Composite_Raw"] = 0.5 * df["Idx_Area_Scaled"] + 0.5 * df["Idx_Pop_Scaled"]
df["SIGMA_Risk_Index"] = min_max(df["Composite_Raw"])

# ====== SẮP XẾP VÀ XUẤT KẾT QUẢ ======
df_final = df[["Country", "Raw_Lambda", "SIGMA_Risk_Index", "WRI_2026"]].sort_values(by="SIGMA_Risk_Index", ascending=False).reset_index(drop=True)
df_final["Absolute_Dev"] = (df_final["SIGMA_Risk_Index"] - df_final["WRI_2026"]).abs()

print("\n" + "="*80)
print("       BẢNG ĐỐI CHIẾU CHỈ SỐ RỦI RO THIÊN TAI TỔNG HỢP SIGMA VS WRI 2026       ")
print("="*80)
print(f"{'Quốc gia':<15} | {'λ Gốc':<8} | {'SIGMA Index':<13} | {'WRI 2026':<10} | {'Độ lệch (abs)':<12}")
print("-"*80)
for idx, row in df_final.iterrows():
    print(f"{row['Country']:<15} | {row['Raw_Lambda']:<8.2f} | {row['SIGMA_Risk_Index']:<13.2f} | {row['WRI_2026']:<10.2f} | {row['Absolute_Dev']:<12.2f}")
print("="*80)

# Xuất file CSV
df_final.to_csv("SIGMA_Climate_Risk_Report.csv", index=False)
print("\n[Thông báo] Đã xuất file dữ liệu sạch: SIGMA_Climate_Risk_Report.csv")
