#vd 8
n=int (input ("Nhập chiều cao:"))
for i in range (n):
    for j in range (n) :
        if (j==0) or (i==j )or (j== n-1):
            print ("*", end='')
        else:
            print (" ",end=' ')
    print ()
