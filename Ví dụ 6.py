#vd 6 Nhập 5 số dương, tính và in ra trung bình của 5 số đó. Chương trình sẽ thoát khi nhập số âm.
count = sum = 0
print ('Nhập danh sách các số dương để tính trung')
while count < 5:
    val = float (input ('Nhập số: '))
    if val < 0:
        print ('Số 0 sai quy tắc, thoát phần mềm')
        break
    count += 1
    sum += val
else:
    print ('Trung Binh =', sum/count)
