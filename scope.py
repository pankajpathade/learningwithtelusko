a = 10

def something():
    a = 5
    b = 7
    print("inside fun",a)
    print(b)

something()
print("outside fun",a)

def anything():
    global a
    a = 14
    print("this is now global variable", a)

anything()
print(a)


def global_var():
    y = 66
    x =globals()['a']
    print(id(x))

    print("in a global_var", y)   

global_var()
print(id(a))