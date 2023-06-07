def factotial(n):
    result =1
    for i in range(2, n+1):
        result *=i
    return result
number = 5
result = factotial(number)
print("Factorial of", number,"is:", result)