# Python program to
# demonstrate numeric value

Integers:

a = 5
print("Type of a: ", type(a))

Float:

b = 5.0
print("\nType of b: ", type(b))

Complex Numbers:

c = 2 + 4j
print("\nType of c: ", type(c))

Output:

Type of a:  <class 'int'>

Type of b:  <class 'float'>

Type of c:  <class 'complex'>


String:

# Python Program for
# Creation of String

# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)
print(type(String1))

# Creating a String
# with triple Quotes
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
print(type(String1))

# Creating String with triple
# Quotes allows multiple lines
String1 = '''Geeks
                For
                Life'''
print("\nCreating a multiline String: ")
print(String1)

Output:
String
with the use of Single Quotes:
    Welcome
    to
    the
    Geeks
    World

String
with the use of Double Quotes:
    I
    'm a Geek
<

class 'str'>


String
with the use of Triple Quotes:
    I
    'm a Geek and I live in a world of "Geeks"
<

class 'str'>


Creating
a
multiline
String:
Geeks
For
Life

List:
# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Creating a List with
# the use of a String
List = ['GeeksForGeeks']
print("\nList with the use of String: ")
print(List)

# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)

Output:
Initial
blank
List:
[]

List
with the use of String:
    ['GeeksForGeeks']

List
containing
multiple
values:
Geeks
Geeks

Multi - Dimensional
List:
[['Geeks', 'For'], ['Geeks']]
Tuple:
# Creating an empty tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a Tuple with
# the use of Strings
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple with the
# use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

# Creating a Tuple
# with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

Output:
Initial
empty
Tuple:
()

Tuple with the use of String:
    ('Geeks', 'For')

Tuple using List:
(1, 2, 4, 5, 6)

Tuple with the use of function:
    ('G', 'e', 'e', 'k', 's')

Tuple with nested tuples:
    ((0, 1, 2, 3), ('python', 'geek'))


Boolean

# Python program to
# demonstrate boolean type

print(type(True))
print(type(False))

Output:
<class 'bool'>

<class 'bool'>


Set:


# Python program to demonstrate
# Creation of Set in Python

# Creating a Set


set1 = set()
print("Initial blank Set: ")
print(set1)

# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)

Output:
Initial
blank
Set:
set()

Set with the use of String:
    {'F', 'o', 'G', 's', 'r', 'k', 'e'}

Set with the use of List:
    {'Geeks', 'For'}

Set with the use of Mixed Values
{1, 2, 4, 6, 'Geeks', 'For'}

Dictionary:

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)
Output:
Empty
Dictionary:
{}

Dictionary with the use of Integer Keys:
    {1: 'Geeks', 2: 'For', 3: 'Geeks'}

Dictionary with the use of Mixed Keys:
    {1: [1, 2, 3, 4], 'Name': 'Geeks'}

Dictionary with the use of dict():
    {1: 'Geeks', 2: 'For', 3: 'Geeks'}

Dictionary with each item as a pair:
    {1: 'Geeks', 2: 'For'}
