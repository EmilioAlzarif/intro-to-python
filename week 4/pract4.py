dic =   {"name":"Armen", "age": 15, "grades": [10 , 8, 8, 4, 6, 7],}

if "weight" not in dic:
    n= int(input("please enter the weight: "))
    w= {"weight": n}
    dic.update({"weight": n})
    print(dic)
else:
    print(dic["weight"])
