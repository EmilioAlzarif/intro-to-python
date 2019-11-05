import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type= str, help = "please enter text with odd number of characters and the length should be 7 or more")

args = parser.parse_args()

x= len(args.text) / 2
x1= int(x-1)
x3= int(x+2)

y= args.text[x1:x3]

print("The old string: ", args.text)
print("Middle 3 characters: ", y)
print("The new string: ", args.text.replace(y, y.upper()))