import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type= str)

args = parser.parse_args()
x= args.text.replace('usa', 'Armenia')
x= x.replace('USA', 'Armenia')
print("The given string :", args.text)
print("The USA/usa count is :", args.text.lower().count('usa'))
print("The new string: ", x)