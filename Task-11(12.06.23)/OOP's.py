#1
class Dog:
 # class attribute
    attr1 = "mammal"
 # Instance attribute
    def __init__(self, name):
        self.r = name
 # Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 # Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
 # Accessing instance attributes
print("My name is {}".format(Rodger.r))
print("My name is {}".format(Tommy.r))
#2
class Dog:
 # class attribute
    attr1 = "mammal"
 # Instance attribute
    def __init__(my, name):
        my.name = name
         
    def speak(my):
        print("My name is {}".format(my.name))
 # Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()
#3
class Dog:                
 
 def __init__(self, dogBreed,dogEyeColor): 
  
    self.breed = dogBreed   
    self.eyeColor = dogEyeColor
 
tomita = Dog("Fox Terrier","brown")
 
print("This dog is a",tomita.breed,"and his eyes are",tomita.eyeColor)
#4
class Dog:  
 
 def __init__(self):
    self.Legs = 4
 
tomita = Dog()
 
print("This dog has",tomita.Legs,"legs")
#5
class Dog:                
 
 def __init__(self, dogBreed="German Shepherd",dogEyeColor="brown"): 
  
    self.breed = dogBreed   
    self.eyeColor = dogEyeColor
 
tomita = Dog()
 
print("This dog is a",tomita.breed,"and his eyes are",tomita.eyeColor)


