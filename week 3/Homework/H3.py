t1 = (1, True, "a", -2, "Anna")       #1

t1= t1[:1] + t1[2:]
print(t1)                             #2

t2 = (1, 2, 3, 4, 5)                  
print(t2)                             #3

t3 = t1[:2] + t2[:3]
print(t3)                             #4

print(t3[2])                          #5

t4 = ([(1,3,5), (8,9), ("Anna", "Bob", "Alice")])
print(t4[0][1])                       #6          