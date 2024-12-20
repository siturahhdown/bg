print("What is the first variable?")
x = input()
print("What is the second variable?")
y = input()
print(f"Original values: 1) {x} 2) {y}")
temp = x
x = y
y = temp
print(f"The variables have been swapped and the first variable is now {x} and second is {y}")