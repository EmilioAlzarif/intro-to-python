import argparse

parser = argparse.ArgumentParser()

s3= {12, 45, 123, 46}


parser.add_argument("val", type=int)
args = parser.parse_args()

if args.val < max(s3) and args.val > min(s3):
    print("true")
else:
    print("false")