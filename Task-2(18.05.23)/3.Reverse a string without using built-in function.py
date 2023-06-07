str="Python"
print("input string",str)
reversed_String=""
count=len(str)
while count>0:
    reversed_String+=str[count-1]
    count=count-1
    print("output string:",reversed_String)