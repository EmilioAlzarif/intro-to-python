correct_num = 5
x = 0
guess = int(input("Guess the correct number: "))
while x<10:
    if guess == correct_num:
        print("That was a good guess!")
        break
    else:
        guess = int(input("Wrong guess, try again: "))
        x += 1
    

    

