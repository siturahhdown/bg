def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 + num2
    print(f"The answer is {answer}")

def sub():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 - num2
    print(f"The answer is {answer}")

def mul():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 * num2
    print(f"The answer is {answer}")

def div():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    answer = num1 / num2
    print(f"The answer is {answer}")

def ask():
    ans = input("Do you want to continue? (yes/no) ")
    if ans.lower() == "yes":
        return True
    else:
        return False
    

while True:
    print(f"""Options:
        1) addition
        2) subtraction
        3) multiplying
        4) division
        5) exit
        """)
    input_ = input("Enter your choice: ")
    if input_ == 1:
        add()
        ask()
    elif input == 2:
        sub()
        ask()
    elif input == 3:
        mul()
        ask()
    elif input == "4":
        div()
        ask()
    elif input == 5:
        print("Quitting program..")
        break
    else:
        print("Invalid Option. Please select a valid option (1-5).")
        continue

