#String:
#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello".
print("Hello")
print('Hello')
#Output:
Hello
Hello
#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Output:
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.

#Slicing
b = "Hello, World!"
print(b[2:5])
#Output:
llo
#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])
#Output:
Orl
#Uppercase:
a = "Hello, World!"
print(a.upper())
#Output:
HELLO WORLD!
#Lowercase:
a = "Hello, World!"
print(a.lower())
#Output:
hello world!
#Replace string:
a = "Hello, World!"
print(a.replace("H", "J"))
Output:
Jello, World!
#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
#Output:
HelloWorld
String Format
age = 36
txt = "My name is John, I am " + age
print(txt)
#Output:
#we can’t add string and number.
TypeError: must be str, not int
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#using format method {} can add number in the string.
#Output:
My name is John, and I am 36
Escape character:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#Output:
#We are the so-called "Vikings" from the north.
#Variables:
#Variables are containers for storing data values.
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
#Exampe codes:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Output:
Orange
Banana
Cherry

x = y = z = "Orange"
print(x)
print(y)
print(z)
#Output:
Orange
Orange
Orange
#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#Output:
apple
banana
cherry
#Output Variable:
x = 5
y = "John"
print(x + y)
#output:
TypeError: unsupported operand type(s) for +: 'int' and 'str'
#Example:
x = 5
y = "John"
print(x, y)
#Output: 5 John

// i have added a plain text
