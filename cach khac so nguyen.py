DS=[]
def NhapDS():
    n=int(input('Nhap so phan tu cua danh sach: '))
    global DS
    DS=[0]*n
    for i in range(0,n):
        DS[i]= int(input('Phan tu thu {0} cua danh sach: '.format(i+1)))   
def Solonnhat(DS):
    solonnhat=0
    for i in DS:
        if solonnhat < i:
            solonnhat = i
        print('Phan tu lon nhat la: ',solonnhat)
    ret
NhapDS()
print('day so vua nhap la: ',DS)
solon=Solonnhat(DS)
print(solon)

                   
