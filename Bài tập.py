#bài 1 Vẽ sơ đồ thuật toán và viết chương trình cho bài toán: nhập vào số km đi được x, tính tiền taxi t phải trả và xuất kết quả
x= float(input('Nhap so km di duoc:'))
if x <0 :
    print('khong the tinh duoc')
else:
    if x<=1 :
        t=15000
    else:
        if x<=5:
            t=15000+13500*(x-1)
        else:
            if 5<x<=120 :
                t=15000+13500*4+11000*(x-5)
            else:
                t=(15000+13500*4+11000*(x-5))*0.9
print('Tien Taxi phai tra:',t)
#bài 2 Vẽ sơ đồ thuật toán và viết chương trình cho bài toán: giải phương trình bậc 2 có dạng ax2 + bx + c = 0.

a = float(input('Nhap a:'))
b = float(input('Nhap b:'))
c = float(input('Nhap c:'))
dta = b*b - 4*a*c
if a == 0:
    print('Phuong trinh bac 1(bx+c=0)')
    if b == 0: 
        if c == 0: 
            print('Phuong trinh vo so nghiem')
        else:
            print('Phuong trinh vo nghiem')
    else:
        x = -c/b
        print('Phuong trinh co nghiem', x)
else:
    if dta < 0: 
        print ('Phuong trinh vo nghiem')
    else:
        if dta == 0:
            x = -b / (2*a)
            print('Phuong trinh co nghiem', x) 
        else:
            x1 = (-b + dta**(1/2)) / (2*a) 
            x2 = (-b - dta**(1/2)) / (2*a) 
            print('Phuong trinh co nghiem', x1, x2)
#bài 4 Vẽ sơ đồ thuật toán và viết chương trình cho bài toán: nhập vào một năm t,
#kiểm tra năm t có phải năm nhuận không và xuất kết quả. Cho ràng buộc sau: năm 
#nhuận là năm chia hết cho 4, không chia hết cho 100 nhưng chia hết cho 400
t = int(input('Nhap nam t: '))
if t % 4 == 0: 
    if t % 100 == 0: 
        if t % 400 == 0: 
            print('Nam', t, 'la nam nhuan') 
        else:
            print('Nam', t, 'khong phai la nam nhuan') 
    else:
        print('Nam', t, 'la nam nhuan') 
else:
    print('Nam', t, 'khonng phai la nam nhuan')
#bài 5 Vẽ sơ đồ thuật toán và viết chương trình cho bài toán: xếp loại các học sinh 
#theo điểm trung bình với điểm trung bình nhập vào từ bàn phím, xuất ra kết quả
dtb=float(input('Nhap diem trung binh:'))
if dtb >10:
    print('Loi')
else:
    if dtb <9:
        if dtb <8:
            if dtb<6.5:
                if dtb<5:
                    if dtb<3.5:
                      if dtb>=0:
                         print('Kem')
                      else:
                          print('Loi')  
                    else:
                        print('Yeu')
                else:
                    print('Trung Binh')
            else:
                print('Kha')
        else:
            print('Gioi')
    else:
        print('Xuat sac')
#bài 6:Vẽ sơ đồ thuật toán và viết chương trình cho bài toán: nhập vào một số tiền t
#(là bội số của 50.000), hãy đổi số tiền ra các mệnh giá và xuất ra tương ứng với số tờ
#tiền ít nhất. Biết rằng có các mệnh giá sau: 500.000, 200.000, 100.000, 50.000.
t=int(input('Nhao so tien:'))
t1=0
t2=0
t3=0
t4=0
if t%50000==0:
     if t>= 500000:
        t1=t//500000
        t=t%500000
     if t>=200000:
        t2=t//200000
        t=t%200000
     if t>=100000:
        t3=t//100000
        t=t%100000
     if t>=50000:
        t4=t//50000
     print('So to menh gia 500000',t1)
     print('So to menh gia 200000',t2)
     print('So to menh gia 100000',t3)
     print('So to menh gia 50000',t4)

else:
    print('Loi')
#bài 7: Vẽ sơ đồ thuật toán và viết chương trình cho bài toán: Nhập chỉ số điện p. Tính tiền điện t. Thuế giá trị gia tăng là 10%.
p=int(input('Nhap chi so dien:'))
if p<1:
    print('Loi')
else:
    if p<=50:
        y= p*1484
    else:
        if p<= 100:
            y= (50*1484)+((p-50)*1533)
        else:
            if p<=200:
                y= (50*1484)+(50*1533)+((p-100)*1786)
            else:
                if p<=300:
                    y= (50*1484)+(50*1533)+(100*1786)+((p-200)*2242)
                else:
                    if p<=400:
                        y= (50*1484)+(50*1533)+(100*1786)+(100*2242)+((p-300)*2503)
                    else:
                        y=(50*1484)+(50*1533)+(100*1786)+(100*2242)+(100*2503)+((p-400)*2587)
t=(y*0.1)+y
print('Tien dien la:',t)
$ git clone https://github.com/nttuanhce/Co-so-Lap-trinh

                        
                    
        

