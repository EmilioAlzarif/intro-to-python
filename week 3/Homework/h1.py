a = [1, 4, 5, 7, 8, -2, 0, -1]        # 1
print(a[3], a[5])                     # 2

a_sorted = a.copy()
a_sorted.sort(reverse = True)

print(a)
print(a_sorted)                      # 3
print(a_sorted[1:4], a_sorted[2:7])  # 4

a_sorted.pop(2)                      
a_sorted.pop(3)                      # 5
print(a_sorted)                      # 6

b = ["grapes", "Potatoes", "tomatoes","Orange", "Lemon", "Broccoli", "Carrot", "Sausages"] # 7

b_sorted = b.copy()
b_sorted.sort()
print(b_sorted)                       #8

c = list()
c += a[1:4] + b[4:7]                  #9
print(c)                              #10
