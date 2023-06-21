class myclass:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def fun(self):
        print(self.__name,self.age)
    def fun1(self,myname):
        self.__name=myname
        
my=myclass("virat",32)
my.fun()
my.fun1("dhoni")

my.fun()


##
##
##class myclass:
##    def __init__(self,name,age):
##        self.__name=name
##        self.age=age
##    def fun(self):
##        print(self.__name,self.age)
##    def fun1(self):
##        print(self.__name)
##        self.__name=name
##        print(self.__name)
##my=myclass("virat",32)
##my.name=(__name,"dhoni")
##my.age=24
##my.fun1()
##my.fun()
##
##
##class Taxi`:
##    def __init__(self, model, capacity, variant):
##        self.__model = model      
##        self.__capacity = capacity
##        self.__variant = variant
##
##    def getModel(self):          
##        return self.__model
##
##    def getCapacity(self):        
##        return self.__capacity
##
##    def setCapacity(self, capacity):  
##        self.__capacity = capacity
##
##    def getVariant(self):        
##        return self.__variant
##
##    def setVariant(self, variant):  
##        self.__variant = variant
##
##class Vehicle(Taxi):
##
##    def __init__(self, model, capacity, variant, color):
##         
##        super().__init__(model, capacity, variant)
##        self.__color = color
##
##    def vehicleInfo(self):
##        return self.getModel() + " " + self.getVariant() + " in " + self.__color + " with " + self.getCapacity() + " seats"
##
##
##
##v1 = Vehicle("i20 Active", "4", "SX", "Bronze")
##print(v1.vehicleInfo())
##print(v1.getModel())


##class myclass:
##    def __init__(self,name,age):
##        self.__name=name
##        self.age=age
##    def 
##        return self.__name
##my=myclass("virat",32)
##print(my.__name)
