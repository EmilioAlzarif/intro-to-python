list1= ['Anna', 'Edgar']
list2= ['Anna', 'Edgar', 'Emilio', 'Jack', 'John', 'Yxia']
def decorator(func):
    def wrapper(*args):
        print("Before calling the function: ", list1)
        func(*args)
        print("After calling the function: ", list1)
    return wrapper

@decorator
def add_values(list2):
    for x in list2:
        if x not in list1:
                list1.append(x)
add_values(list2)
