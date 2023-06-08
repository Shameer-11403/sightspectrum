#dictionary
dss={1:"geeks",2:"for",3:"geeks"}
sr=dss.copy()#copy create a new dict of items after changing the existing dict.
del sr[2]
print(dss)
print(sr)

var={"car":"bmw","bike":"ducati","hi":"hello"}
var.clear()#clear shows the empty{} after clearing dict.
print(var)


var={"car":"bmw","bike":"ducati","hi":"hello"}
x = var.get("car")#getting a particular key-value.
print(x)

var={"car":"bmw","bike":"ducati","hi":"hello"}
x=var["car"]
print(x)
x=var.items()
print(x)
var["car"]="mustang"
print(x)

var={"car":"bmw","bike":"ducati","hi":"hello"}
var.update({"geek":"geeks"})#update arguments should be inside the {}.
print(var)

var={"car":"bmw","bike":"ducati","hi":"hello"}
var.pop("car")#pop won't run without arguments
print(var)

var={"car":"bmw","bike":"ducati","hi":"hello"}
var.popitem()#popitem takes no arguments,and only remove the last key&value.
print(var)


var={"car":"bmw","bike":"ducati","hi":"hello"}
del var["car"]#without the list value error occurs because the dict is no longer exists.
print(var)


var = {"name":{1:{"surname":["s","m","n"]}},"jega":{1:{"surname":["s","m","n"]}}}
var["jega"][1]["surname"][2]="m"
print(var)

import json
var = '{"country":"india"}'
json.loads(var)
print(var)
json.dumps(var)
print(type(var))

#lambda
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

