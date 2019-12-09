def Alarm(day):
    assert day != "Sunday", "I won't Wake you up today!"
    return "Wake up It's "+ day+ "!"
print(Alarm("Monday"))
print(Alarm("Sunday"))