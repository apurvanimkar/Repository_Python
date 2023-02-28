
#The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Apurva", 36)
print(p1.name)
print(p1.age)

#The __str__() Function
class Person:
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return self.name 

p1 = Person("Rohn")
print(p1)

#Object Methods
class Person:
  def __init__(self, name):
    self.name = name
    def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Rohn")
p1.myfunc()
