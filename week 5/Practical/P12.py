def power(max):
    for x in range(max + 1):
        yield 2**x
value = power(5)
print(list(value))