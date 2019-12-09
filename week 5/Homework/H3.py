def f1(func):
    def wrapper(*args):
        print("Before the function")
        func()
        print("After the function")
    return wrapper
@f1
def text():
    print("Inside the Function")

text()
