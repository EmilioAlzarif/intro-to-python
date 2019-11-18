def decor1(func):
    def wrapper(*args):
        return func().lower().capitalize()
    return wrapper

def decor2(func):
    def wrapper(*args):
        return func() + "!!! Welcome to the party."
    return wrapper

@decor2
@decor1
def f1():
    return "HI EVERYONE"

print(f1())
