def adminfunc(user, **kwargs):
    if user == "admin":
        print("Welcome Mr.", user, "opening your secret list now :")
        for key, value in kwargs.items():
            print(key, " : ", value)    
    else:
        print("access denied for the user: ", user)
user= "admin"
adminfunc(user, potato="vegetable", banana="fruit", chicken="meat")
user= "Jesus"
adminfunc(user, potato= "vegetable", banana= "fruit", chicken= "meat")