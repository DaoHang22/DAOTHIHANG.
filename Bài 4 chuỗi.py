def Nhap():
    Kytu = input('Nhap ki tu: ')
    return Kytu
def Xuatma(Kytu):
    if Kytu:
        Ma = ord(Kytu)
        print('Ma cua ki tu la:', Ma)
    else:
        print('Chuoi rong, nhap lai.')
        
#Ham chinh
Makytu= True
while Makytu:
    Kytu = Nhap()
    Xuatma(Kytu)
    if ord(Kytu)== 27 :
        print('Thoat!')
        break
    tieptuc = input('Co muon tiep tuc khong? Nhap Y de tiep tuc: ',)
    if tieptuc=='Y' or tieptuc=='y':
        Makytu = True
    else:
        Makytu = False
