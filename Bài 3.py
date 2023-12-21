n=int(input('Nhap n: '))
i=1
if n>0:
    for i in range (0,n):
        if i%2 != 0:
            print(i)
        i=i+1
else:
    print('Loi!')
