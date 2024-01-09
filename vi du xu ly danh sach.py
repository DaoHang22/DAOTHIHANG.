print('*'*35)
lst=[5,7,2,9,6,3,10,17,16]
for x in lst:#duyet theo tung phan tu (collection)
    print(x,end='\t') #end='\t' la ket thuc bang 1 dau tab va in theo hang ngang
print()#print khong co tham so thi mac dinh la xuong dong
print('*'*35)
for i in range(len(lst)):#duyet theo chi so i (index)
    x=lst[i] # i la chi so index vi tri i cua phan tu
    print(x, end='\t')
print()
print('*'*35)
for i in range(len(lst)-1,-1,-1):
    x=lst[i]
    print(x, end='\t')
print()
a=[10,20,30,40]
b=a
print(b)
b[2]=50
print(a)
print()
a=6
b=a
b=10
print(a)
print()
lst=[10,20,30,40]
print(lst)
lst.insert(,10)
print(lst)

