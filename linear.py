
pos =-1
def search(lst,n):
    i=0
    
    while i < len(lst):
        if lst[i]==n:
            globals()["pos"]=i
            return True   
        i+=1         
    return False

lst=[1,6,8,3,9,5]
n=10

if search:
    print("found at",pos+1)
else:
    print("not found")