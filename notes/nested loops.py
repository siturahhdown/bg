#adding loops in another
#for x in range(4):
#    for y in range(3):
#       print(f"{x},{y}")

#numbers = [5, 2, 5, 2, 2]
#for count in numbers:
 #   print('x' * count)

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)