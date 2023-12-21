#Vd2 Viết chương trình nhập vào một số nguyên dương,
#nếu nhập sai yêu cầu nhập lại. Khi nhập đúng thì xuất ra
#tổng từ 1 đến n
print('Nhap N: ')
n=int(input())
s=0
i=1
while i<=n:
    s=s+i
    i=i+1
print('Tong = ',s)
