last_number = int(input("\nPlease enter the last number up till which sum of prime number is to be found:"))
print("We will find the sum of prime numbers in python upto", last_number)
sum=0
for number in range(2, last_number):
    i=2
    for i in range(2,number):
        if(int(number%i)==0):
            i=number
            break;
    if i is not number:
        sum = sum +number
print("\nThe sum of prime numbers in python from 1 to ", last_number,"is :",sum)