import math

# ====== HỆ SỐ TỐI ƯU TỪ MÔ HÌNH ======
a0 = 35
a1 = 5
a2 = 0
a3 = 0
a4 = -5
a5 = 0

# ====== DỮ LIỆU THỰC TẾ (CẦN THAY BẰNG DỮ LIỆU THẬT) ======
# Danh sách các cơn bão với các thông số:
# [SST, Pmin, Humidity, Shear, MonsoonIndex, Vmax_thuc_te]
du_lieu_bao = [
    [28.5, 985, 75, 10, 0.3, 120],  # Bão 1
    [27.0, 990, 70, 15, 0.2, 95],   # Bão 2
    [29.5, 975, 80, 8, 0.5, 140],   # Bão 3
    [28.0, 988, 78, 12, 0.4, 110],  # Bão 4
    [29.0, 980, 82, 9, 0.6, 130],   # Bão 5
    [30.0, 970, 85, 7, 0.7, 150],   # Bão 6
    [27.5, 992, 72, 14, 0.2, 105],  # Bão 7
    [28.8, 983, 76, 11, 0.4, 125],  # Bão 8
    [29.2, 978, 80, 10, 0.5, 135],  # Bão 9
    [29.8, 972, 83, 8, 0.6, 145],   # Bão 10
]

print("\n" + "="*60)
print("🌪️ ÁP DỤNG MÔ HÌNH DỰ BÁO BÃO VÀO DỮ LIỆU THỰC TẾ")
print("="*60)

tong_sai_so = 0
so_luong = len(du_lieu_bao)

for i, bao in enumerate(du_lieu_bao):
    SST, Pmin, Humidity, Shear, MonsoonIndex, Vmax_thuc = bao
    
    # Dự báo bằng mô hình
    Vmax_du_bao = a0 + a1*SST + a2*Pmin + a3*Humidity + a4*Shear + a5*MonsoonIndex
    if Vmax_du_bao < 0:
        Vmax_du_bao = 0
    
    # Sai số
    sai_so = abs(Vmax_thuc - Vmax_du_bao) / Vmax_thuc * 100
    tong_sai_so += sai_so
    
    # In kết quả
    print(f"\n📌 Bão {i+1}:")
    print(f"   SST: {SST}°C, Pmin: {Pmin}hPa, Độ ẩm: {Humidity}%, Gió cắt: {Shear}m/s")
    print(f"   Vmax thực tế: {Vmax_thuc} km/h")
    print(f"   Vmax dự báo:  {Vmax_du_bao:.1f} km/h")
    print(f"   Sai số:       {sai_so:.2f}%")

# Sai số trung bình
sai_so_tb = tong_sai_so / so_luong
print("\n" + "="*60)
print(f"📊 KẾT QUẢ TỔNG HỢP:")
print(f"   Số cơn bão: {so_luong}")
print(f"   Sai số trung bình: {sai_so_tb:.2f}%")
print("="*60)
