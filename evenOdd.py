def evenOdd(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[23,54,35,67,78,44,88,86]
even,odd =evenOdd(lst)
print(even)
print(odd)