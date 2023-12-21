n = int(input("Nhap n: "))
m = int(input("Nhap m: "))

while m!=0:
    if m == 0:
        print(' UCLN: ' , n)
        break
    if n == 0:
        print(' UCLN: ' , m)
        break
    if m > n:
        m = m % n
    else:
        n = n % m
else:
    print("UCLN cua m va n la: ",  n )

