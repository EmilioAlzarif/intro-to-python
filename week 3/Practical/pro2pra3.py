import sys
list2 = sys.argv[1:]
print(list2)

list1 = ["hello", 1, True]
list3 = list1.copy()

list3.extend(list2)
print(list3)
print(list1)