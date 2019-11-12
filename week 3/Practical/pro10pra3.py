import argparse

parser = argparse.ArgumentParser()

s2= {12, 45, 123, 46}


parser.add_argument("val", type=int)
args = parser.parse_args()

print(s2)

if args.val in s2:
    s2.remove(args.val)
    print(s2)