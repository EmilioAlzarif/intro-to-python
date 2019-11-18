def gradeavg(name, *args):
    grades = 0
    if len(args)<1:
        print("No grades available for ", name)
    else:
        for x in args:
            grades+= x
        print(name," your average grade is: ", grades/len(args))
name= "Emilio"
gradeavg(name, 21, 9, 31, 42, 54, 65)
gradeavg(name)