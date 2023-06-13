
#Creating a class using keyword class:
class MyClass:
    x = 5
print(MyClass)

#creating p1 as object:
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

#__init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

#p1.age=40 is modified

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)

#pass to avoide error

class Person:
  pass
