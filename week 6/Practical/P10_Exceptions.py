list1 = ["a", 0, 2]
for x in list1:
    try:
        print("The current entry of the list is:", x)
        print("The reciprocal of", x, "is ", 1/x )
    except Exception as e:
        print("Oops!", e)