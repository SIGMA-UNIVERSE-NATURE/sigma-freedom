# Dữ liệu lũ lụt tỷ đô (2016-2025)
floods_actual = [2, 4, 2, 3, 3, 4, 2, 3, 4, 4]

# Phân loại năm bão mạnh (dựa trên dữ liệu bão thực tế)
# 2017 (Harvey, Irma, Maria), 2020 (Sally), 2021 (Ida)
strong_storm_years = [1, 5, 9]  # index trong danh sách (2017, 2021, 2025)

# Tính λ cho từng nhóm từ dữ liệu 2016-2020
train_years = floods_actual[:5]  # 2016-2020
train_indices = [0, 1, 2, 3, 4]

lambda_strong = []
lambda_normal = []

for i, year in enumerate(train_years):
    if i in strong_storm_years:
        lambda_strong.append(year)
    else:
        lambda_normal.append(year)

lambda_strong = sum(lambda_strong) / len(lambda_strong) if lambda_strong else 0
lambda_normal = sum(lambda_normal) / len(lambda_normal) if lambda_normal else 0

# Dự báo cho giai đoạn kiểm tra (2021-2025)
test_years = floods_actual[5:]  # 2021-2025
test_indices = [5, 6, 7, 8, 9]

predicted = []
for i, year in enumerate(test_years):
    if test_indices[i] in strong_storm_years:
        predicted.append(lambda_strong)
    else:
        predicted.append(lambda_normal)

# Tính sai số
errors = []
for i in range(len(test_years)):
    err = abs(test_years[i] - predicted[i]) / test_years[i] * 100
    errors.append(err)

print("\n" + "="*60)
print("📊 DỰ BÁO LŨ LỤT CẢI TIẾN (MÔ HÌNH KẾT HỢP)")
print("="*60)
print(f"\n🌊 LŨ LỤT TỶ ĐÔ:")
print(f"   λ cho năm bão mạnh: {lambda_strong:.2f} sự kiện/năm")
print(f"   λ cho năm bình thường: {lambda_normal:.2f} sự kiện/năm")
print(f"   Sai số từng năm (2021-2025): {[f'{e:.2f}%' for e in errors]}")
print(f"   Sai số trung bình: {sum(errors)/len(errors):.2f}%")

# So sánh với mô hình cũ
old_errors = [30.00, 40.00, 6.67, 30.00, 30.00]
new_errors = errors
print(f"\n📉 So sánh với mô hình cũ:")
print(f"   Sai số cũ: {sum(old_errors)/len(old_errors):.2f}%")
print(f"   Sai số mới: {sum(new_errors)/len(new_errors):.2f}%")
print(f"   Cải thiện: {((sum(old_errors) - sum(new_errors)) / sum(old_errors) * 100):.2f}%")
