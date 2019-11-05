import datetime
import time
import calendar
bday= datetime.date(1993, 11, 2)
tdy= datetime.date.today()

print("My Birthday date: ", bday)
print("My Birthday year: ", bday.year)
print("My Birthday month: ", bday.month)
print("My Birthday day: ", bday.day)
print("My Birthday weekday: ", bday.weekday())
nextbday= datetime.date(2020, 11, 2)
print("Days left till my BirthDay: ", nextbday-tdy)
x= calendar.month(2017, 1)
print("the Calendar of May 2017: ", x)
tdelta= datetime.timedelta(days= 1)
print("Yesterday's date and time: ", tdy-tdelta)
x1= tdy-tdelta
print("Add 2 days to yesterday’s date and time: ", x1 + tdelta * 2)
print("Subtract 3 days from yesterday’s date and time: ", x1 - tdelta * 3)

