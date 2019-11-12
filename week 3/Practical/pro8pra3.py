import argparse

parser = argparse.ArgumentParser()

s1= {12, 45, "hi", 45, 123, 45}


parser.add_argument("val", type=int)
args = parser.parse_args()

print(s1)
s1.add(args.val)
print(s1)
