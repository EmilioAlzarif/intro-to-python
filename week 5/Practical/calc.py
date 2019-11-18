import pretty_print as pr

def calculate_cube(x):
    return x**3

def calculate_square(x):
    return x**2

def main():
    pr.simple_print(calculate_square(2))
    pr.pro_print(calculate_cube(4))

if __name__ == '__main__':
    main()