class A:
    def show(self):
        print(" in A show")

class B(A):
    def show(self):
        print(" in B show")# this is called method overriding

a =B()
a.show()