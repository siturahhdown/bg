captive = False
not_captive = False

if captive:
    print("The prisoner is held captive")
elif not_captive:
    print("The prisoner is not held captive")
else:
    print("Unkown...")

print("Enjoy your day!")


user_input = input("Do you have good credit? (yes/no): ").strip().lower()
price = 1000000
good_credit = user_input == 'yes'
bad_credit = not good_credit  # Assuming if not good, then it's bad credit

if good_credit:
    down_payment= 0.1* price
elif bad_credit:
    down_payment= 0.2* price
else: 
    print("Unkown...")

print(f"Downpayment: £{down_payment}")