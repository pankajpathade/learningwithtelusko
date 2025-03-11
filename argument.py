def person(*b):
    c=0
    for i in b:
        c+=i
    print(c)


person(1,2,4,5)

def status(name,**data):
    print(name)
    print(data)

status(name="rahul",age=25,city="pune",no=796)

def mall(name,**data):
    for i,j in data.items():
        print(name)
        print(i,j)

mall(name="phoeix",road="nagar",cap=2500,court=True)
    