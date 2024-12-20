temp = int(input("What is the temprature outside?"))
if temp > 30:
    print("It's hot outside.")
else:
    print("It's not hot outside.")

while True:
    password = input("What is your password?")
    if 3 < len(password) <9:
       print("Password is valid")
       break
    else:
        print("Password is incorrect")
        continue

while True:
    phone = int(input("What is your phone number?"))
    if 0 < len(phone) >11:
        print("Phone number is valid")
        break
    else:
        print("Phone number is incorrect")
        continue
