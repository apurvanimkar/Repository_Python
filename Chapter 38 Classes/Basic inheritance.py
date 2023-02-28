#Single Inheritance

class Father:
    money=1000

    def show(self):
        print("parent class")

    @classmethod
    def showmoney(cls):
        print("parent class method",cls.money)

class son(Father):
    def disp(self):
        print("child class inherited")

s=son()
s.disp()
s.show()
s.showmoney()
