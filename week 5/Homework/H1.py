def max(*args):
    if len(args) == 0:
        print("No numbers are given")
    else:
        list= []
        for x in args:
            list.append(x)
        list = sorted(list)
    print(list[-1])
max(12, 21312, 2, 123, 42, 436)

