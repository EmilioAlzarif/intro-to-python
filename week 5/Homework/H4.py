def dec1(func):
    def wrapper(*args):
        return func() + ", it's me! "
    return wrapper

def dec2(func):
    def wrapper(*args):
        return "<u>" + func() + "</u>"
    return wrapper

@dec2
@dec1
def text():
    return " Hi"
print(text())
    