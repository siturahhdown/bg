# Exceptions
while True:
    try:
        age = int(input("age: "))
        income = 20000
        risk = income / age
        print(age)
    except ValueError:
        print("Invalid value") #if the user inputs a string, it will throw an error

        # crashed with ZeroDivisionError this is because the user inputed 0 this means we can use try and except to catch the error
    except ZeroDivisionError:
        print("Age cannot be 0")
        break

