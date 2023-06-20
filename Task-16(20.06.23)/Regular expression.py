import re
var="hi i'm a freasher guy"
x=re.findall("[a-s]",var)
print(x)

import re
var="sfsd234ljfk"
x=re.findall("\d",var)
print(x)

import re
var="hello planet"
x=re.findall("he..o",var)
print(x)

import re
var="hello planet"
x=re.findall("^hello",var)
print(x)

import re
var="hello planet"
x=re.findall("planet$",var)
print(x)

import re
var="hello planet"
x=re.findall("he.?o",var)#followed by 0 or 1
print(x)

#split
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#sub()
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#Match object
#span
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
#string
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
#group
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
