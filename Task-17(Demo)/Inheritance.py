1-------
class A:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
class B(A):
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
class C(B):
    def feature(self):
        print("Feature 5 working")
a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature3()
b1.feature4()

c1=C(A,B)
c1.feature()
2---------
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()
3-----------
 Python code to demonstrate how parent constructors
 are called.
 
 parent class
class Person(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
     
 child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
 
 
 creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
 calling a function of the class Person using
 its instance
a.display()
a.details()




        
