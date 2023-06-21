#Working of read() mode:----------------------------------

# Python code to illustrate read() mode
file = open("demo.txt", "r")
print(file.read())

# Python code to illustrate read() mode character wise
file = open("file.txt", "r")
print (file.read(5))

#Creating a file using write() mode:---------------------

# Python code to create a file
file = open('file.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

#Working of append() mode:-------------------------------

# Python code to illustrate append() mode
file = open('file.txt', 'a')
file.write("This will add this line")
file.close()

# Python code to illustrate with()----------------------
with open("file.txt") as file: 
    data = file.read()
# do something with data

#Using write along with the with() function:-------------

# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
    f.write("Hello World!!!")



##Example:-------------------------------------------------
    
f=open("demo.txt","r+")
print(f.read())
# a file named "geek", will be opened with the reading mode.

file = open('demo.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)

file = open('demo.txt','r')
file = open('demo.txt','w')
file.write("1354272627")
var="khiusdjdsbsjd"
file.write(var)
file.close()

file=open('demo.txt','w+')
file.write("sjfkdkasafsd")
file.write("FJSHFFFFfag")
file.close()

with open("demo.txt", "r+") as file:
    contents = file.read()

# Modify the contents by adding your text
new_contents = contents + "\nYour additional text here."
print(new_contents)

