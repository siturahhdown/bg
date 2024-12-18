numbers = [5, 2, 1, 7, 4, 5, 2]  # Example list with duplicates
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)