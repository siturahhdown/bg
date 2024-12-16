name = input("What is your name? ")
surname =input("What is your surname? ")
print("hello", name, "what is your birth year?")
by = int(input())                                         #use int before integers 
print("your birthyear is", by)
age = 2024 - by
print("You are", age, "years old")
print("what is your weight?(kg)")                      #converting weight
weight = int(input())
print("Your weight in grams is", weight*1000)
msg = f"""Fullname: {name} {surname} 
DOB: {by} Age: {age}   
Bodyweight: {weight}Kg {weight*1000}g"""                      #formatted lines
print(msg)

























