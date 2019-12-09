list1= [1, 2, 43, 5, 213, 4]
def list_func(list1):
    for x in list1:
        yield x
value = list_func(list1)
print(value)
print(next(value))