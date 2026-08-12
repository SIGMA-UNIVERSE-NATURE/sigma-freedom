import math

# ==== DỮ LIỆU MÔ PHỎNG (cần thay bằng dữ liệu thực tế) ====
# Vmax thực tế (km/h)
Vmax_thuc = [120, 95, 140, 110, 130, 150, 105, 125, 135, 145]

# Các biến đầu vào
SST = [28.5, 27.0, 29.5, 28.0, 29.0, 30.0, 27.5, 28.8, 29.2, 29.8]
Pmin = [985, 990, 975, 988, 980, 970, 992, 983, 978, 972]
Humidity = [75, 70, 80, 78, 82, 85, 72, 76, 80, 83]
Shear = [10, 15, 8, 12, 9, 7, 14, 11, 10, 8]
MonsoonIndex = [0.3, 0.2, 0.5, 0.4, 0.6, 0.7, 0.2, 0.4, 0.5, 0.6]

# ====== TÌM HỆ SỐ TỐI ƯU BẰNG PHƯƠNG PHÁP THỬ ======
best = None
best_error = 999

# Thử các giá trị cho a0, a1, a2, a3, a4, a5
for a0 in range(-50, 51, 5):
    for a1 in range(-5, 6):
        for a2 in range(-5, 6):
            for a3 in range(0, 6):
                for a4 in range(-5, 6):
                    for a5 in range(0, 11):
                        # Tính dự báo
                        Vmax_du_bao = []
                        for i in range(len(Vmax_thuc)):
                            v = (a0 + a1*SST[i] + a2*Pmin[i] + a3*Humidity[i] + a4*Shear[i] + a5*MonsoonIndex[i])
                            if v > 0:
                                Vmax_du_bao.append(v)
                            else:
                                Vmax_du_bao.append(0)
                        
                        # Tính sai số trung bình
                        errors = []
                        for i in range(len(Vmax_thuc)):
                            if Vmax_thuc[i] > 0 and Vmax_du_bao[i] > 0:
                                errors.append(abs(Vmax_thuc[i] - Vmax_du_bao[i]) / Vmax_thuc[i] * 100)
                        if errors:
                            avg_error = sum(errors) / len(errors)
                            if avg_error < best_error:
                                best_error = avg_error
                                best = (a0, a1, a2, a3, a4, a5, avg_error)

# ====== KẾT QUẢ ======
print("\n" + "="*50)
print("🌪️ TỐI ƯU HÓA MÔ HÌNH DỰ BÁO BÃO")
print("="*50)
if best:
    print(f"\n✅ Hệ số tối ưu:")
    print(f"   a0 = {best[0]}")
    print(f"   a1 = {best[1]}")
    print(f"   a2 = {best[2]}")
    print(f"   a3 = {best[3]}")
    print(f"   a4 = {best[4]}")
    print(f"   a5 = {best[5]}")
    print(f"\n📊 Sai số trung bình: {best[6]:.2f}%")
else:
    print("\n⚠️ Không tìm thấy bộ hệ số tối ưu.")
print("="*50)
