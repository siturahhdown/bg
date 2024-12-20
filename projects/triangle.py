import time

print("""
 _________  ________  ___  ________  ________   ________  ___       _______            
|\___   ___\\   __  \|\  \|\   __  \|\   ___  \|\   ____\|\  \     |\  ___ \     
\|___ \  \_\ \  \|\  \ \  \ \  \|\  \ \  \\ \  \ \  \___|\ \  \    \ \   __/|      
     \ \  \ \ \   _  _\ \  \ \   __  \ \  \\ \  \ \  \  __\ \  \    \ \  \_|/__      
      \ \  \ \ \  \\  \\ \  \ \  \ \  \ \  \\ \  \ \  \|\  \ \  \____\ \  \_|\ \     
       \ \__\ \ \__\\ _\\ \__\ \__\ \__\ \__\\ \__\ \_______\ \_______\ \_______\   
        \|__|  \|__|\|__|\|__|\|__|\|__|\|__| \|__|\|_______|\|_______|\|_______|                                                                                                                                                                                          
      """)

while True:
    try:
        base = float(input("What is the base in cm? "))
        height = float(input("What is the height in cm? "))
    except ValueError:
        print("Invalid input. Please enter numeric values for base and height.")
        continue

    area = 0.5 * base * height
    print(f"""The area of the triangle is {area} cm^2
Height: {height}
Base: {base}
""")
    
    cont = input("Do you want to do another one? (yes/no) ")
    if cont.lower() == "no":
        print("Closing...")
        time.sleep(1)
        print("Goodbye")
        break
    elif cont.lower() == "yes":
        print("Continuing...")
        continue
    else:
        print("Invalid input. Please enter yes or no.")