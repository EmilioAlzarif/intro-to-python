import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type= str)
parser.add_argument("first_word", type= str)
parser.add_argument("second_word", type= str)
args = parser.parse_args()

print("enter a text please : ", args.text)
print("choose a word you want to change from the text : ", args.first_word)
print("choose a new word : ", args.second_word)
print(args.text.replace(args.first_word, args.second_word))