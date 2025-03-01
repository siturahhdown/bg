import time

exit = False

def age_calculator():
     age = 2025 - DOYB
     print(f"Your age is {age}")

def full_sheet():
    print(f"""
    Full Name: {first_name} {second_name}
    DOYB: {DOYB}
    Age: {age}
    Full Address: {full_address}
    """)

def continuing():
    log = input("Would you like to restart? ")
    if log.lower == "yes":
        print("Restarting...")
        exit = True
    else:
        print("Closing application...")
        time.sleep(2)
        

while True:
    print("Data File Generator")
    first_name = input("What is your first name? ")
    second_name = input("What is your second name? ")
    print("What is the year you were born in?")
    DOYB = int(input())
    age = age_calculator()
    print("What is your current home address?")
    full_address = input()
    full_sheet()
    continuing()
    if exit == False:
        continue
    else:
        break
    


