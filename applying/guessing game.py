secretnumber = 9
guess_count = 0
guess_limit = 3
while guess_count <  guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secretnumber:
        print("You won")
        break
    elif guess_count == 3:
         print("You lost")
         break
    else:
        print("Try again")
        

