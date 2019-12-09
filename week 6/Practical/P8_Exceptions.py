def div(x,y):
    try:
        return x/y
    except Exception as e:
        print(e)
print(div(10,2))
div(5,0)