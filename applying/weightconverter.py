while True:
    print("What is your current weight?")
    weight = int(input())
    unit = input("""
                (L)Lbs
                (K)Kg
                """)
    if unit.upper() == "L":
        converted = weight * 0.45359237
        print(f"You weigh {converted}pounds")
    else:
        converted = weight / 0.45
        print(f"You weigh {converted}kg")
        break