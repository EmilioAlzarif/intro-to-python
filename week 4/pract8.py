list1 = [5, 7, -7, "abc", 2, 4, True, 3, 4, 6, 7, 7]
for x in range(len(list1)): 
    print("x = ", list1[x]) # if we need the indexes we can put only x instead of list1[x]  :) 
    if list1[x] == 3:
        break