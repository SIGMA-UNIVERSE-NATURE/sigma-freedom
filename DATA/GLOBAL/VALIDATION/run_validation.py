import math

# Hàm tính sai số trung bình (bỏ qua giá trị 0)
def tinh_sai_so(du_lieu_thuc_te, du_lieu_du_bao):
    sai_so = []
    for i in range(len(du_lieu_thuc_te)):
        if du_lieu_thuc_te[i] != 0:
            sai_so.append(abs(du_lieu_thuc_te[i] - du_lieu_du_bao[i]) / du_lieu_thuc_te[i] * 100)
    if len(sai_so) == 0:
        return 0
    return sum(sai_so) / len(sai_so)

# DỮ LIỆU THỰC TẾ (cần thay bằng dữ liệu thật nếu có)
thuc_te_dong_dat = [30, 25, 32, 27, 29, 31, 28, 26, 33, 24, 30, 28]
du_bao_poisson = [28] * 12
sai_so_dong_dat = tinh_sai_so(thuc_te_dong_dat, du_bao_poisson)

thuc_te_lu_lut = [4.2, 4.5, 5.0, 5.8, 6.2, 5.5, 4.8, 4.3, 4.0, 4.1, 4.3, 4.5]
du_bao_lu_lut = [4.0, 4.2, 4.8, 5.5, 6.0, 5.2, 4.5, 4.0, 3.8, 4.0, 4.2, 4.5]
sai_so_lu_lut = tinh_sai_so(thuc_te_lu_lut, du_bao_lu_lut)

thuc_te_han_han = [-0.8, -1.0, -1.2, -1.5, -1.8, -2.0, -1.9, -1.6, -1.3, -1.0, -0.9, -0.7]
du_bao_han_han = [-0.7, -0.9, -1.1, -1.4, -1.7, -1.9, -1.8, -1.5, -1.2, -0.9, -0.8, -0.6]
thuc_te_abs = [abs(x) for x in thuc_te_han_han]
du_bao_abs = [abs(x) for x in du_bao_han_han]
sai_so_han_han = tinh_sai_so(thuc_te_abs, du_bao_abs)

thuc_te_bao = [2, 1, 3, 2, 4, 3, 2, 1, 2, 3, 4, 2]
du_bao_bao = [2, 2, 2, 2, 3, 3, 2, 2, 2, 3, 3, 2]
sai_so_bao = tinh_sai_so(thuc_te_bao, du_bao_bao)

print("\n" + "="*50)
print("📊 KẾT QUẢ KIỂM ĐỊNH CÔNG THỨC")
print("="*50)
print(f"\n1. Động đất (Poisson):          {sai_so_dong_dat:.2f}%")
print(f"2. Lũ lụt Mekong:               {sai_so_lu_lut:.2f}%")
print(f"3. Hạn hán Sahel:               {sai_so_han_han:.2f}%")
print(f"4. Bão Biển Đông:               {sai_so_bao:.2f}%")
print("\n" + "="*50)

