def sum(x,y):
    assert type(x)==int and type(y)==int, "Arguments of type int required"
    return x+y
print(sum(2, 4))
print(sum(2,"4"))