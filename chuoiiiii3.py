def Nhap():
    print('Nhap chuoi: ')
    chuoi = ""
    while True:
        ki_tu = input("Nhap ki tu: ")
        if ki_tu != '.':
            chuoi = chuoi + ki_tu
            break
        else:
            break
    return chuoi

def Dem(chuoi):
    chu_hoa = 0
    chu_thuong = 0
    chu_so = 0
    khac = 0
    for ki_tu in chuoi:
        if ki_tu in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            chu_hoa = chu_hoa + 1
        elif ki_tu in ['a','b','c','d','x','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']:
            chu_thuong = chu_thuong + 1
        elif ki_tu in ['1','2','3','4','5','6','7','8','9','0']:
            chu_so = chu_so + 1
        else:
            khac = khac + 1
    return chu_hoa, chu_thuong, chu_so, khac

def Xuat(chuoi):
    chu_hoa, chu_thuong, chu_so, khac = Dem(chuoi)
    print('So chu hoa: ', chu_hoa)
    print('So chu thuong: ', chu_thuong)
    print('So chu so: ', chu_so)
    print('So ki tu khac: ', khac)

def demmax(chuoi):
    chu_hoa, chu_thuong, chu_so, khac = Dem(chuoi)
    demmax = max(chu_hoa, chu_thuong, chu_so, khac)
    if demmax == chu_hoa:
        print('Loai ki tu nhieu nhat la chu hoa')
    elif demmax == chu_thuong:
        print('Loai ki tu nhieu nhat la chu thuong')
    elif demmax == chu_so:
        print('Loai ki tu nhieu nhat la chu so')
    elif demmax == khac:
        print('Loai ki tu nhieu nhat la ki tu khac')

# Ham chinh
thongke = True
while thongke:
    chuoi = Nhap()
    Xuat(chuoi)
    demmax(chuoi)
    tieptuc = input('Co muon tiep tuc khong? Nhap Y de tiep tuc: ')
    if tieptuc == 'Y' or tieptuc == 'y':
        thongke = True
    else:
        thongke = False
