username = input("Input some name please ")
try:
    if username == "Rambo":
        raise Exception
except Exception:
    print("Rambo is an invalid username")
else:
    print("Welcome", username)