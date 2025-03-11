import sys
print(sys.setrecursionlimit(100))
print(sys.getrecursionlimit())

i=0
def greet():
    global i
    i+=1
    print("Hello")
    greet()

greet()