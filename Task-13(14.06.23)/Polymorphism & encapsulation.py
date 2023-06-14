#Polymorphism:

#Different classes with the same method:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

#Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


#Encapsulation:

#Public Members:
  class Circle:
    def __init__(self, radius):
        self.radius = radius  # Public attribute

    def calculate_area(self):
        return 3.14 * self.radius * self.radius  # Public method


my_circle = Circle(5)
print(my_circle.radius)  # Accessing public attribute
print(my_circle.calculate_area())  # Calling public method

#Protected Members:

class Person:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def _display_name(self):  # Protected method
        print("Name:", self._name)


class Student(Person):
    def display_student_details(self):
        self._display_name()  # Accessing protected method


student = Student("John")
student.display_student_details()  # Calling protected method

#Private Members:

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def __display_balance(self):  # Private method
        print("Balance:", self.__balance)


my_account = BankAccount("123456789", 1000)
# print(my_account.__account_number)  # Error: AttributeError
# my_account.__display_balance()  # Error: AttributeError

    
