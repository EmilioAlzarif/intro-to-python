import sys
list2 = sys.argv[1:]
print(list2)

list1 = ["hello", 1, True]

list1.extend(list2)
print(list1)