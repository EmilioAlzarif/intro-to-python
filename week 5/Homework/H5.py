def my_range(n):
    for x in range(n + 2):
        if x == n + 1:
            return "There are no values left"
        yield x
values = my_range(10)
print(next(values))