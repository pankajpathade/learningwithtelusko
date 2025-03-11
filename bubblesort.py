def sort(numb):
    for i in range(len(numb)-1,0,-1):
        for j in range(i):
            if numb[j]<numb[j+1]:
                temp=numb[j]
                numb[j]=numb[j+1]
                numb[j+1]=temp




numb=[1,44,3,6,5,7,42,87,122,645,22,4,62,2]
sort(numb)
print(numb)