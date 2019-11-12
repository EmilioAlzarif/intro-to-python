import argparse

parser = argparse.ArgumentParser()

list2 = [2, 213, 2, 54, 2]

parser.add_argument("val", type=int)
args = parser.parse_args()


print(list2)
print("nubmer of ", args.val, "s is :  ", list2.count(args.val))