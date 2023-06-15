#Inheritance:--------------------
#1-------------
class myclass:
    def __init__(self,course,fee):
        self.course=course
        self.fee=fee
    def fun1(self):
        print(self.course,self.fee)
        
class myclass1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun3(self):
        print(self.name,self.age)
        
class myclass2(myclass, myclass1):
    def __init__(self,course,fee):
        self.course=course
        self.fee=fee
    def fun(self):
            print(self.course,self.fee)
            myclass.__init__(self,"data",200)
            myclass1.__init__(self,"sam",23)
my = myclass2("virat",23)
my.fun()
my.fun1()
my.fun3()

#2---------------------------

class myclass:
    def __init__(self,name,age):
        self.a=name
        self.b=age
    def fun(self):
        print(self.a,self.b)
my=myclass("virat",35)
my.b=20
my.a="vijay"
print(my.a)

##3---------------------------
##taking output from inside the function
class myclass:
    def __init__(self,country,state):
        self.country=country
        self.state=state
        
    def fun(self):
        print(self.country,self.state)
        
class myclass1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.object=myclass("tamilnadu","india")
        self.object.fun()
    def fun1(self):
        print(self.name,self.age)

my=myclass1("virat",34)
my.fun1()
#4----------------------------
class myclass:
    def __init__(self,course,fee):
        self.course=course
        self.fee=fee
    def fun1(self):
        print(self.course,self.fee)
        
class myclass1(myclass):
    def __init__(self,name,age):
        super().__init__("java",56)
        self.name=name
        self.age=age
        
    def fun3(self):
        print(self.name,self.age)
my=myclass1("hi",23)
my.fun3()
my.fun1()
        
#5-------------------------------

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#Abstraction----------------------------
#1---------------------------
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    @abstractmethod
    def another_abstract_method(self):
        pass


from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass
#2-------------------------------------
class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

