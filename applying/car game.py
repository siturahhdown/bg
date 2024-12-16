import time
command = ""
i = 0
car_started = False
while True:
    command = input("Enter a command: ").lower() #lower allows it not needed to make us repeat ourselves
    if command == "start":
        if car_started:
            print("Car is already started!")
        else:
            print("The car is starting...")
            time.sleep(2)
            print("Car has started")
            car_started = True
    elif command == "stop" :
        if not car_started:
           print("The car is stopping...")
           time.sleep(3)
           print("Car stopped!")
        else:
            print("The car is already stopped!")
            car_started = False
    elif command =="help":
        print("""Available commands:
                 start
                 stop
                 quit
                """)
    elif command == "quit":
        for i in range(4): # Loop to print three dots
            print("."*i, end="", flush=True)  # Print a dot without a newline
            time.sleep(1)  # Wait for 1 second
            i += 1  # Increment the counter
        print("\nGoodbye!")  # Print goodbye message after the loop
        break
    else:
        print("Sorry, I didn't understand that command.")
