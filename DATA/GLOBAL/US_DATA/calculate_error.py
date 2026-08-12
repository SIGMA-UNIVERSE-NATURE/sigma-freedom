# Dữ liệu cháy rừng thực tế (2016-2025) - từ NIFC (NASA)
wildfires_actual = [67743, 71499, 58083, 50477, 58950, 58985, 68988, 56580, 61685, 72068]

# Dữ liệu lũ lụt tỷ đô (2016-2025) - từ NOAA
floods_actual = [2, 4, 2, 3, 3, 4, 2, 3, 4, 4]

# Chọn 5 năm đầu để tính lambda (2016-2020)
train_wildfires = wildfires_actual[:5]  # 2016-2020
train_floods = floods_actual[:5]

# Tính lambda trung bình từ 5 năm đầu
lambda_wildfire = sum(train_wildfires) / 5
lambda_flood = sum(train_floods) / 5

# Dự báo cho 5 năm sau (2021-2025)
predicted_wildfires = [lambda_wildfire] * 5
predicted_floods = [lambda_flood] * 5

# Tính sai số trung bình cho phần kiểm tra (2021-2025)
test_wildfires = wildfires_actual[5:]  # 2021-2025
test_floods = floods_actual[5:]

errors_wildfire = []
errors_flood = []

for i in range(5):
    err_w = abs(test_wildfires[i] - predicted_wildfires[i]) / test_wildfires[i] * 100
    err_f = abs(test_floods[i] - predicted_floods[i]) / test_floods[i] * 100
    errors_wildfire.append(err_w)
    errors_flood.append(err_f)

# Kết quả
print("\n" + "="*60)
print("📊 SAI SỐ DỰ BÁO (2021-2025) DỰA TRÊN DỮ LIỆU NASA")
print("="*60)

print(f"\n🔥 CHÁY RỪNG:")
print(f"   λ (từ 2016-2020): {lambda_wildfire:.0f} vụ/năm")
print(f"   Sai số từng năm: {[f'{e:.2f}%' for e in errors_wildfire]}")
print(f"   Sai số trung bình: {sum(errors_wildfire)/5:.2f}%")

print(f"\n🌊 LŨ LỤT TỶ ĐÔ:")
print(f"   λ (từ 2016-2020): {lambda_flood:.2f} sự kiện/năm")
print(f"   Sai số từng năm: {[f'{e:.2f}%' for e in errors_flood]}")
print(f"   Sai số trung bình: {sum(errors_flood)/5:.2f}%")
