class A:
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B(A):
    def feature3(self):
        print("feature 3 is wworking")

    def feature4(self):
        print("feature 4 is working")

class C(B):
    def feature5 (self):
        print("feature 5 is working")
              
c1 = C()
c1.feature1()