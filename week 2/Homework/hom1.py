import argparse
import datetime
import time

parser = argparse.ArgumentParser()

parser.add_argument("--num_y", type= int)
parser.add_argument("--num_d", type= int)
args = parser.parse_args()
tdy= datetime.datetime.today()
tdelta= datetime.timedelta(days= 0)
print("Current date : ", tdy)

if args.num_y:    
    tdeltay= tdelta + datetime.timedelta(days= args.num_y * 365)
 
if args.num_d:
    tdeltad= tdelta + datetime.timedelta(days= args.num_d + 1)

x = tdeltay + tdeltad
print("Given days :", args.num_d)
print("Given years :", args.num_y)
print("Final date :", tdy + x)