while True:
    x = "Made by Titas"
    name = input("What is your current goverment name? ")
    print(f"Your goverment name is {name}")
    print("What is your date of birth year?")
    yr = int(input())
    age = 2024 - yr
    print(f"Your age is {age} born in {yr}")
    print("What is your current home address? ")
    addi = input()
    print(f"Your home address is {addi}")
    weight = input("What is your weight in kg? ")
    print("Do you want to change your goverment name?")
    change = input()
    if change == "yes":
        name = input("What is your new goverment name? ")
        print(f"Your goverment name is {name}")
        break
    elif change == "no":
        print("Your name was not changed")
        break
    else:
        print("Invalid input...")
        continue
print(f"""
FullName: {name}
DOB: {yr}
Age: {age}
Home Address: {addi}
Weight: {weight}kg

{x}
""")



