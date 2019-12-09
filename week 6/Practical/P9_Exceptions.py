def div(x,y):
    try:
        return x/y
    except ZeroDivisionError as e:
        print(e)
print(div(10,2))
div(5,0)