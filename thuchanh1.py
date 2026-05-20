# Nhập tổng tiền hóa đơn
tong_tien = int(input("Nhập tổng tiền hóa đơn (VND): "))

# Kiểm tra điều kiện giảm giá
if tong_tien >= 500000:
    giam_gia = tong_tien * 0.10
else:
    giam_gia = 0

# Tính số tiền cần thanh toán
thanh_toan = tong_tien - giam_gia

# Hiển thị kết quả
print("Số tiền giảm giá:", int(giam_gia), "VND")
print("Số tiền khách phải trả:", int(thanh_toan), "VND")