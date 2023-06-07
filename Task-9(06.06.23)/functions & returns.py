def function():
    print("function")
function()#function calling

def function(a,b):
    print("adding",a+b)
function(2,3)#function with argument

def function(a,b=2):#function with default argument
    print("adding",a+b)
function(2)

def function(b,a=3):#function with default argument
    print("adding",a+b)
function(2)


def function(name,age):#function with default argument
    print("my name is", name,"age is",age)
function("sri",23)

def function(age,name):#function with default argument
    print("my name is", name,"age is",age)
function(name="sri",age=23)

def function(*age):#function with * argument-accepts only many datas 
    print("age is",age)
function("sri",25)


def function(**age):#function with ** argument-accept values with variable
    print("age is",age)
function(a="sri",b=25)



def fun(m1,m2,m3):
    var=m1+m2+m3
    return var
var1 = fun(22,43,54)
if  var1> 10:
    print("success")
else:
    print("failure")
      




def fun(m1,m2,m3):
    var=m1+m2+m3
    print(var)
fun(22,43,54)




def fun(m1,m2,m3):
    var=m1+m2+m3
    return var
var1 = fun(22,43,54)
if var1>179:
    print("sucess")
else:
   print("failure") 


