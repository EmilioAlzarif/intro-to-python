import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type=str)
parser.add_argument("start_index", type=int)
parser.add_argument("end_index", type=int)
args = parser.parse_args()
z=args
print("The given text: ", z.text)
print("Start index: ", z.start_index)
print("End index: ", z.end_index)

print("Output string: ", z.text[z.start_index:z.end_index])