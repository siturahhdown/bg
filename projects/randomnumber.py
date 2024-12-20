import random
import time

while True:
    start = input("Would you like to start? ")
    if start.lower() == "yes":
        print("Pick a random number between 1 to 100")
        number = int(input())
        ans = random.randint(1,100)
        if number == ans:
            print("You guessed it right!")
            time.sleep(1)
            print("you get too live with system 32 in your pc for another day!")
            print()
            break
        else:
            print(f"You guessed wrong, it was {ans} while you picked {number}")
            break
    elif start.lower == "no":
        print("Goodbye...")
        time.sleep(2)
        break
    else:
        print("Invalid input, please enter yes or no")
        continue
