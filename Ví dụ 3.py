#Vd3 nhập số n nguyên dương. Tính tổng các số
#chẵn từ 0 đến n và in tổng ra màn hình 
n=int (input ("Mời nhập sô:"))
S=0
if n % 2==0:
    for x in range (2, n+1,2) :
        s=s+x
elif n%2!=0:
    for x in range (1, n+1,2) :
        s=s+x
print ("Tống s=", s)
