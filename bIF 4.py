n=int(input("Nhap n: "))
m=int(input("Nhap m: "))
bay= False
while bay == False:
        if m==n:
                UCLN = m
                break
        if m==0:
                UCLN = n
                break
        if n==0:
                UCLN = m
                break

        if m>n:
                m=m%n
        else:
                n=n%m
print('UCLN la: ', UCLN)
