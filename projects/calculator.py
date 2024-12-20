add = False
sub = False
mul = False
div = False

while True:
    try:
        selecter = int(input("""
        Options:
        1) addition
        2) subtraction
        3) multiplying
        4) division
        5) exit
        """))
        
        if selecter < 1 or selecter > 5:
            print("Invalid option. Please select a valid option (1-5).")
            continue

        if selecter == 1:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            add = True
            answer = num1 + num2
            print(f"The answer is {answer}")
        
        elif selecter == 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            sub = True
            answer = num1 - num2
            print(f"The answer is {answer}")
        
        elif selecter == 3:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            mul = True
            answer = num1 * num2
            print(f"The answer is {answer}")
        
        elif selecter == 4:
            num1 = float(input("What is your first number: "))
            num2 = float(input("What is your second number: "))
            div = True
            answer = num1 / num2
            print(f"The answer is {answer}")

        elif selecter == 5:
            print("Quitting program..")
            break

        quit = input("Do you want to quit the program? (yes/no) ")
        if quit.lower() == "yes":
            break

    except ValueError:
        print("Invalid input. Please enter a number.") 