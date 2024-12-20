numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight,",
    "9": "nine",
    "0": "zero"
}

while True:
    phone = input("Phone: ")
    if phone.lower() == "quit":  # Use parentheses to call the method
        print("Bye")
        break
    elif len(phone) != 11:  # Check if the length is not equal to 11
        print("Invalid input..")
        continue
    else:
        for digit in phone:
            word = numbers[digit]  # Convert each digit to its word
            print(word, end=" ")
        print()  # Print a newline after the output
        
        