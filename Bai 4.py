n=int(input("Nhap n: "))
m=int(input("Nhap m: "))
while m>0 and n>0:
    if m==n:
        UCLN=m
    else:
        if m==0:
            UCLN=n
        else:
            if n==0:
                UCLN=m
            else:
                if m>n:
                    m=m%n
                else:
                    n=n%m
print("UCLN cua m va n la: ", max(m, n))
