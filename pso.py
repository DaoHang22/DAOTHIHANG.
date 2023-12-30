import math
#hàm nhập phân số
def nhap():
    print("Nhap phan so: ")
    tu = int(input("Nhap tu so: "))
    mau = int(input("Nhap mau so: "))
    while mau == 0:
        print("Mau so khac 0. Nhap lai: ")
        mau = int(input("Nhap mau so: "))
    return tu,mau
#hàm xuất phân số
def xuat(tu,mau):
    print('Phan so la: {0}/{1}'.format(tu,mau))
# Hàm tìm ước chung lớn nhất của hai số
def UCLN (a, b) :
    a=math.fabs(a)
    b=math.fabs(b)
    while a!=b:
        if a==0:
            UCLN=b
            break
        elif b==0:
            UCLN=a
            break
        elif a>b:
            a=a%b
        else:
            b=b%a
    else:
        UCLN=a
    return UCLN
# Hàm tìm bội chung nhỏ nhất
def bcnn(a, b):
    a=math.fabs(a)
    b=math.fabs(b)
    bcnn=(a * b) /UCLN(a,b)
    return bcnn
# Hàm tối giản phân số
def toigian(tu,mau):
    tu2=int(tu/UCLN(tu,mau))
    mau2=int(mau/UCLN(tu,mau))
    return tu2,mau2
# Hàm làm đẹp
def lamdep(tu,mau):
    if tu ==0:
        print('Ket qua la: {0}'.format(tu))
    elif mau==1:
         print('Ket qua la: {0}'.format(tu))
    elif tu==mau:
        tu=1
        print('Ket qua la: {0}'.format(tu))
    elif tu==-mau:
        tu=-1
        print('Ket qua la: {0}'.format(tu))
    elif mau<0:
        tu,mau= toigian(-tu,-mau)
        if mau==1:
             print('Ket qua la: {0}'.format(tu))
        else:
            xuat(tu,mau)
    else:
        xuat(tu,mau)
    
#Hàm cộng hai phân số
def cong(tus1,maus1,tus2,maus2):
    tus1,maus1=toigian(tu1,mau1)
    tus2,maus2=toigian(tu2,mau2)
    mau=int( bcnn(maus1, maus2))
    tu= int((tus1 * mau/maus1+ tus2*mau/maus2))
    print('Ket qua phep cong la: {0}/{1}'.format(tu,mau))
    lamdep(tu,mau)
#Hàm trừ hai phân số
def tru(tus1,maus1,tus2,maus2):
    tus1,maus1=toigian(tu1,mau1)
    tus2,maus2=toigian(tu2,mau2)
    mau= int(bcnn(maus1, maus2))
    tu= int((tus1 * mau/maus1- tus2*mau/maus2))
    print('Ket qua phep tru la: {0}/{1}'.format(tu,mau))
    lamdep(tu,mau)
# Hàm nhân hai phân số
def nhan(tu1,mau1,tu2,mau2):
        tu1,mau1=toigian(tu1,mau1)
        tu2,mau2=toigian(tu2,mau2)
        tu=int( tu1 * tu2)
        mau=int(mau1 * mau2)
        print('Ket qua phep nhan la: {0}/{1}'.format(tu,mau))
        lamdep(tu,mau)
# Hàm chia hai phân số
def chia(tu1,mau1,tu2,mau2):
    tu1,mau1=toigian(tu1,mau1)
    tu2,mau2=toigian(tu2,mau2)
    if tu2!= 0:
            tu=int( tu1 * mau2)
            mau=int(mau1*tu2)
            print('Ket qua phep chia la: {0}/{1}'.format(tu,mau))
            toigian(tu,mau)
            lamdep(tu,mau)
    else:
        print( "Không thể chia cho 0.")
tu1,mau1=  nhap()
tu2,mau2=nhap()
phanso1=xuat(tu1,mau1)
phanso2=xuat(tu2,mau2)
uc1=UCLN(tu1,mau1)
print (' UCLN cua {0} va {1} la {2}'.format(tu1,mau1,uc1))
uc2=UCLN(tu2,mau2)
print (' UCLN cua {0} va {1} la {2}'.format(tu1,mau1,uc2))
bc1=bcnn(mau1,mau2)
print (' BCNN cua {0} va {1} la {2}'.format(tu1,mau1,bc1)) 
tuso1,mauso1= toigian(tu1,mau1)
xuat(tuso1,mauso1)
lamdep(tu1,mau1)
lamdep(tu2,mau2)
cong(tu1,mau1,tu2,mau2)
tru(tu1,mau1,tu2,mau2)
nhan(tu1,mau1,tu2,mau2)
chia(tu1,mau1,tu2,mau2)




