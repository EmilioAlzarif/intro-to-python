def iter_num(n):
    for x in range(n + 1):
        if(x>0):
            yield x
values = iter_num(20)
print(list(values))    