def calculate_average(numbers):
    total = sum(numbers)
    average = total/len(numbers)
    return average
my_list =[2,4,6,8,10]
result = calculate_average(my_list)
print("Average:",result)