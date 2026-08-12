import math

# Dữ liệu thực tế 12 tháng
thuc_te = [30, 25, 32, 27, 29, 31, 28, 26, 33, 24, 30, 28]

def tinh_sai_so(thuc_te, du_bao):
    sai_so = []
    for i in range(len(thuc_te)):
        if thuc_te[i] != 0:
            sai_so.append(abs(thuc_te[i] - du_bao[i]) / thuc_te[i] * 100)
    return sum(sai_so) / len(sai_so) if sai_so else 0

# Thử các giá trị lambda từ 20 đến 35
best_lambda = None
best_sai_so = 100

for lam in range(20, 36):
    du_bao = [lam] * 12
    sai_so = tinh_sai_so(thuc_te, du_bao)
    print(f"λ = {lam:2d} → sai số: {sai_so:.2f}%")
    if sai_so < best_sai_so:
        best_sai_so = sai_so
        best_lambda = lam

print("\n" + "="*40)
print(f"✅ λ tối ưu: {best_lambda} với sai số {best_sai_so:.2f}%")
