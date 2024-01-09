def nhap_va_thong_ke():
    # Nhập dãy kí tự từ bàn phím
    day_ki_tu = input("Nhập dãy kí tự đến khi gặp kí tự '.': ")
    # Khởi tạo các biến đếm
    chu_hoa = 0
    chu_thuong = 0
    chu_so = 0
    khac = 0
    # Duyệt qua các kí tự trong dãy
    for ki_tu in day_ki_tu:
        # Nếu gặp kí tự '.', dừng vòng lặp
        if ki_tu == '.':
            break
        # Nếu là chữ cái viết hoa, tăng biến đếm chu_hoa
        elif ki_tu.isupper():
            chu_hoa += 1
        # Nếu là chữ cái viết thường, tăng biến đếm chu_thuong
        elif ki_tu.islower():
            chu_thuong += 1
        # Nếu là chữ số, tăng biến đếm chu_so
        elif ki_tu.isdigit():
            chu_so += 1
        # Nếu là kí tự khác, tăng biến đếm khac
        else:
            khac += 1
    # In ra kết quả thống kê
    print(f"Số chữ cái viết hoa: {chu_hoa}")
    print(f"Số chữ cái viết thường: {chu_thuong}")
    print(f"Số chữ số: {chu_so}")
    print(f"Số kí tự khác: {khac}")
    # Xác định loại kí tự nhiều nhất
    max_count = max(chu_hoa, chu_thuong, chu_so, khac)
    if max_count == chu_hoa:
        print("Loại kí tự nhiều nhất là chữ cái viết hoa")
    elif max_count == chu_thuong:
        print("Loại kí tự nhiều nhất là chữ cái viết thường")
    elif max_count == chu_so:
        print("Loại kí tự nhiều nhất là chữ số")
    else:
        print("Loại kí tự nhiều nhất là kí tự khác")

# Gọi hàm khi chương trình chạy
if __name__ == "__main__":
    nhap_va_thong_ke()
