pos = -1

def search(lst,n):
    l = 0
    u = len(lst)-1

    while l <= u:
        mid = (l + u)//2
        if lst[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if lst[mid] < n:
                l = mid + 1
            else:
                u = mid -1
    return False

lst=[1,3,5,6,8,22,55,722,994,1227]

n= 55

if search(lst,n):
    print("found at",pos+1)
else:
    print("not found")
            
