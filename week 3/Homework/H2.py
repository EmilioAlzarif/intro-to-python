a1 = ("Cookies", "Chocolate", 8, True, -3, -5,"Chocolate", 8, False, 8)  #1
b1 = (8, True, 10, 14, "Chocolate", "Milk","Jelly", True, False, True)   #2
print(a1)
print(b1)

set_a = set(a1)                                                        #3
set_b = set(b1)                                                        #4
print(set_a)
print(set_b)

union_ab = set_a.union(set_b)                                          #5
intersection_ab = set_a.intersection(set_b)                            #6
print(union_ab)
print(intersection_ab)

union_ab.add("Kit-Kat")
union_ab.add("Oreo")
print(union_ab)                                                        #7

new_set= union_ab | intersection_ab                     
print(new_set)                                                         #8

print("Chocolate" in new_set)                                          #9

new_set.remove("Oreo")
print(new_set)                                                         #10
                                                    




