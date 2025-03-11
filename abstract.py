from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Whiteboard(Computer):
    def write(self):
        print("It's writting")

class Programer:
    def work(self):
        print("solving bug's")
        com1.process()

class Laptop(Computer):
    def process(self):
        print("running")

com1=Laptop()
com2=Whiteboard()
com2.process()
prog1=Programer()
prog1.work()