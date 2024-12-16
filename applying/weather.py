hot = True
cold = False

if hot:
    print("It's hot outside!")
elif cold:
    print("It's cold outside!")
else:
    temp = input("What is the temprature outside?")
    if temp > 20:
        print("It's cold outside!")
    else:
        print("It's hot outside!")
name = input("What is your full name? ")
dob = int(input("Whats your date of birth? "))
age = 2024 - dob
print(f"Hi {name}! You are {age}")