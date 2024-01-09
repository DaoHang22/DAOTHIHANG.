def Nhapdayso():
    dayso = input("Nhap day so nguyen: ")
    lst = dayso.split()
    daysonguyen = []
    for x in lst:
        so = int(x)
        daysonguyen.append(so)
    return daysonguyen
def Xuatdayso(dayso):
    print('Day so nguyen vua nhap la: ')
    print(dayso)
def Solonnhat(dayso):
    solonnhat=0
    for i in dayso:
        if solonnhat < i:
            solonnhat=i
    print('So lon nhat la: ',solonnhat)
def Sonhonhat(dayso):
    nhonhat = min(dayso)
    print ('So nho nhat trong day la: ', nhonhat)
    return nhonhat
def Sapxeptang(dayso):
    dayso=sorted(dayso)
    print('Day so sap xep tang dan la: ',dayso)
def Sapxepgiam(dayso):
    dayso.sort(reverse=True)
    print('Day so sap xep giam dan la: ',dayso)
# Ham chinh
nhapdaysonguyen = True
while nhapdaysonguyen:
    dayso = Nhapdayso()
    Xuatdayso(dayso)
    lonnhat= Solonnhat(dayso)
    nhonhat= Sonhonhat(dayso)
    tang= Sapxeptang(dayso)
    giam= Sapxepgiam(dayso)
    tieptuc = input('Co muon tiep tuc khong? Nhap Y de tiep tuc: ')
    if tieptuc == 'Y' or tieptuc == 'y':
        thongke = True
    else:
        thongke = False
        break

