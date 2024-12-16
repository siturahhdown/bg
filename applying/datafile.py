name = input("What is your first name? ")
surname = input("What is your second name? ")
db = int(input(f"What year were you born {name}? "))
age = (2024-db)
print("Your age is",age)
print("What is your current body weight in KG")
bw = int(input())
height = int(input("What is your height in cm? ")) / 100  # Convert cm to meters

data =f"""
Full Name: {name} {surname}
Age: {age} 
Weight: {bw}
Height: {height}
BMI: {bw/(height**2)}"""
print(data)

msg = f"Your name is {name} and you seem healthy with a weight of {bw}kg"