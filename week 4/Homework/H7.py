list4 = [[10, 20, 40], [40, 50, 60], [70, 80, 90]]

list5 = [x[:-1] + [100] for x in list4]

print(list4)
print(list5)