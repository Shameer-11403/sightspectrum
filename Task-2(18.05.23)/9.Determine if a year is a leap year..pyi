year=int(input("Enter the Year:"))
if(year%4==0 and year%100 or year%400==0):
    print(year,"is a leap year.")
else:
    print(year, " is  not a leap year.")