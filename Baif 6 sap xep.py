for i in range (n-1):
    for j in range (i+1,n):
        if (a[i]>a[j]):
            tam = a[i]
            a[i]=a[j]
            a[j]=tam
