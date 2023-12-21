#Vd1 Viết chương trình yêu cầu nhập vào một số nguyên dương
#[1..10], nếu nhập sai yêu cầu nhập lại. Khi nhập đúng thì
#xuất ra bình phương của giá trị mới nhập vào
value = -1;
while value <1 or value >10:
    value=int(input('Nhap gia tri [1..10]: '))
print('value=',pow(value,2));
