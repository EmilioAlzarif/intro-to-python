menu = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
desert = str(input("please enter the name of the desert you want: "))

while True:
    if desert in menu:
        print("Your desert will arrive in 10 minutes !")
        break
    else:
        desert = str(input("please choose another desert: "))