n= int(input('Nhap n: '))
if n>0:
    i=1
    t=0
    for i in range(1,n+1):#vi range chay tu 1 den can duoi cua n nen phai su dung n+1
        t=t+i
    print(t)
else:
    print("Nhap lai!")

n= int(input('Nhap n: '))
if n>0:
    i=1
    t=0
    while i<=n:
        t=t+i
        i=i+1
    print(t)
else:
    print("Nhap lai!")

n= int(input('Nhap n: '))
if n>0:
    i=1
    t=0
    for i in range(1,n+1):#vi range chay tu 1 den can duoi cua n nen phai su dung n+1
        t=t+i
    print(t)
    i=1 #neu khong gan i va t lai thi ket qua se sai vi lay gia tri o vong for de tinh
    t=0
    while i<=n:
        t=t+i
        i=i+1
    print(t)
else:
    print("Nhap lai!")
