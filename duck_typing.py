class Pycharm:
    def execute(self):
        print("compling")
        print("running")


class Editor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compling")
        print("running")

class Laptop:
    def code(self,ide):
        ide.execute()

    def run(self,ide):
        ide.execute()

ide=Pycharm()

lap1 =Laptop()
lap1.code(ide)

ide=Editor()

lap2=Laptop()
lap2.run(ide)