def NhapDS():
    global n
    n=int(input('Nhap so phan tu cua danh sach: '))
    global DS
    DS=[0]*n
    for i in range(0,n):
        DS[i]= int(input('Phan tu thu {0} cua danh sach: '.format(i+1)))
def XuatDS(DS):
    for i in DS:
        print(i,end=' ')
    print()
def Solonnhat(dayso):
    solonnhat=0
    for i in dayso:
        if solonnhat < i:
            solonnhat=i
    return solonnhat
def Sobenhat(dayso):
    sobenhat=0
    for i in dayso:
        if sobenhat < i:
            sobenhat=i
    return sobenhat
def TangDS(DS):
    for i in range(0,n-1):
        for j in range(i+1,n): 
            if DS[i]>DS[j]:
                tam= DS[i]
                DS[i]=DS[j]
                DS[j]=tam
    return DS
def GiamDS(DS):
    for i in range(0,n-1):
        for j in range(i+1,n): 
            if DS[i]<DS[j]:
                tam= DS[i]
                DS[i]=DS[j]
                DS[j]=tam
    return DS
def FP(DS):
    for i in range(0,n-1):
        if DS[i]==5:
            print(DS[i])
    return i
#CT chinh
DS=[]
n=0
NhapDS()
XuatDS(DS)
print('Phan tu lon nhat la: ',Solonnhat(DS))
print('Tang dan: ',TangDS(DS))
print('Giam dan: ',GiamDS(DS))
print('Phan tu = 5 la:', FP(DS))
