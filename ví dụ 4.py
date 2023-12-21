#VD4 Viết chương trình vòng lặp vĩnh cửu cho phép phần
#mềm chạy liên tục, khi nào hỏi thoát mới thoát phần mềm
while True:
    a=int (input ("Nhập giá trị:"))
    print ("Giá trị bạn nhập ",a)
    s=input ("Tiếp tục phần mềm không? (c/k) :")
    if s=="c":
        break
print ("BYE!")
