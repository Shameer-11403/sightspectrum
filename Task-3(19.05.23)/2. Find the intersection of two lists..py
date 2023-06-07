def intersection(list1,list2):
    list3=[value for value in list1 if value in list2]
    return list3
list1=[1,2,3,4,5]
list2=[0,2,4,6,8]
print(intersection(list1,list2))