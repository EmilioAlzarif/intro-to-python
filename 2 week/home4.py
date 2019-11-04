import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type= str)

args = parser.parse_args()

print("The given string :", args.text)
print("The USA/usa count is :", args.text.lower().count('usa'))
print("The new string: ", args.text.lower().replace('usa', 'Armenia'))