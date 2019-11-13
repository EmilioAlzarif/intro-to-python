d = {"name": "Armen", "age": 15, "grades": [10, 8, 8, 4, 6, 7] }

average = sum(d["grades"]) / len(d["grades"])
print("your average is :", average)
if average > 7:
    print("Good Job")
else:
    print("You need to work more")
