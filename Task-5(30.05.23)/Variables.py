#variable

#Python has no command for declaring a variable.
x = 5
y = "John"
print(x)
print(y)
Output:
5
John


#Casting:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Output:

John
John
John
John
John
John

#Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"

Output:

SyntaxError: invalid syntax