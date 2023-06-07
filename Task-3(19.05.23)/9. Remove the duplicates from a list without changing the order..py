def remove_duplicates_preserve_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
my_list = [1,2,3,2,4,1,5,6,3,4,7,8,5]
result = remove_duplicates_preserve_order(my_list)
print(result)