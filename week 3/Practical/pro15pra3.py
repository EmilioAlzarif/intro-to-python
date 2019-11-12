import argparse

dic1 = {"name":"Emil", "last_name":"Alzarif","age":"26"}
print(dic1)

parser = argparse.ArgumentParser()

parser.add_argument("key", type= str, help = "please enter a key for dictionary")
parser.add_argument("value", type= str,help = "please enter text a value for the key")

args = parser.parse_args()
dic1[args.key]=args.value

print(dic1)