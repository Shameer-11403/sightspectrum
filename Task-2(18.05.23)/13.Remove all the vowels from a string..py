string="hello world"
vowels = ['a','e','i','o','u','A','E','I','O','U']
for char in string:
    if char not in vowels:
        result=char
        print(result)