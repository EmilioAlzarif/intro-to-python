import datetime
import time
import calendar
tdy= datetime.datetime.today()

print("Current date and time: ", tdy)  
print("current year :", tdy.year)
print("current month :", tdy.month)
print("current weekday :", tdy.weekday())
print("current weekday :", tdy.isoweekday())
tdelta= datetime.timedelta(days = 5)
print("date today - 5 =", tdy - tdelta)
print("date today + 5 =", tdy + tdelta)