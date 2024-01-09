def Nhap():
    cannang = float(input('Nhap can nang: '))
    chieucao = float(input('Nhap chieu cao: '))
    return cannang, chieucao

def Tinh(chieucao, cannang):
    BMI = cannang / (chieucao * chieucao)
    print('chi so BMI:',BMI)
    return BMI

def Xuat(BMI):
    if BMI < 18.5:
        print('Gay. Nguy co phat trien benh: Thap')
    elif BMI < 25:
        print('Binh thuong. Nguy co phat trien benh: Trung binh')
    elif BMI < 30:
        print('Hoi beo. Nguy co phat trien benh: Cao')
    elif BMI < 35:
        print('Beo phi cap do 1. Nguy co phat trien benh: Cao')
    elif BMI < 40:
        print('Beo phi cap do 2. Nguy co phat trien benh: Rat cao')
    else:
        print('Beo phi cap do 3. Nguy co phat trien benh: Nguy hiem')

# Ham chinh
Ktra = True
while Ktra:
    cannang, chieucao = Nhap()
    BMI = Tinh(chieucao, cannang)
    Xuat(BMI)
    kt = input('Co muon nhap tiep khong? Nhap tiep bam Y: ')
    if kt == 'y' or kt == 'Y':
        Ktra = True
    else:
        Ktra = False
