class Students:
    def __init__(self,name,rollno):
        self.name =name
        self.rollno =rollno
        self.lap=self.Laptop()
       

    
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand ="hp"
            self.cpu="i5"
            self.ram= 8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Students('navin',2)
s2=Students('jenny',3)
s1.show()