
##class myclass:
##    def __init__(self):
##        print("hgfthh")
##    def fun(self)    
##    
##
##myclass()
###my = myclass()




##class myclass:
##    x= "success"#global variable or class varaiable
##    def __init__(self,name,age):
##        self.my=name
##        self.age=age
##        print("my name is ",self.my,"and my age is ",self.age,self.x)
##    def fun(self):
##        print("my name is ",self.my,"and my age is ",self.age)
##    def funs(self):
##        print("my name is",self.my)
##   
##
##var=myclass("sam",23)
##var.fun()
##var.funs()
##print(myclass.x)

##class myclass:
##    x= "success"#global variable or class varaiable
##    #global variable is used outside the function,and local variable is used inside the function.
##    #we can use the golbal variable inside the function also by using global keyword.
##    def __init__(self,name,age):
##        self.my=name
##        self.age=age
##        print("my name is ",self.my,"and my age is ",self.age,self.x)
##    def fun(self):
##        print("my name is ",self.my,"and my age is ",self.age)
##    def funs(self):
##        print("my name is",self.my)
##    def fun1(a,b):
##        print("ausdf",a,b)
##
##var=myclass("sam",23)
##var.fun()
##var.funs()
##print(myclass.x)

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

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
