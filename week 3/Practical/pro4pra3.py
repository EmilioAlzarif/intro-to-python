import argparse

parser = argparse.ArgumentParser()

list4 = [2, 213, 2, 54, 2]

parser.add_argument("val", type=int)
args = parser.parse_args()


print(list4)
list4.remove(args.val)
print(list4)