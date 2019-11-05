import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text")
args = parser.parse_args()

print("The given string: ", args.text)
print("All lowercase: ", args.text.lower())
print("All uppercase: ", args.text.upper())
