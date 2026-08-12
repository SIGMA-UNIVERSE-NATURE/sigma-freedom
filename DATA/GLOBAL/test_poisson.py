import math

# Dữ liệu thực tế (thay số liệu thật vào)
thuc_te = [30, 25, 32, 27, 29, 31, 28, 26, 33, 24, 30, 28]

# Dự báo Poisson (giả định lambda = 28)
lambda_ = 28
du_bao = [28] * 12

# Tính sai số trung bình
sai_so = []
for i in range(12):
    sai_so.append(abs(thuc_te[i] - du_bao[i]) / thuc_te[i] * 100)

tb_sai_so = sum(sai_so) / 12
print(f"Sai số trung bình: {tb_sai_so:.2f}%")
