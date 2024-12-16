while True:
    print("What is the prisoner's name?")
    prisoner_name = input()
    print("What is the prisoner's crime?")
    crime = input()
    print("What is the prisoner's sentence?")
    sentence = input()

    print(f"Prisoner's name: {prisoner_name} Crime committed: {crime} Sentence given: {sentence} yrs")
    print("Do you want to proceed with this information? (yes/no)")
    proceed = input().strip().lower()

    if proceed == "yes":
        print("Information has been recorded")
        print("Generating data file...")
        print(f"""
Prisoner name: {prisoner_name}
Crime committed: {crime}
Sentence given: {sentence} yrs
""")
        break  # Exit the loop if they want to proceed
    elif proceed == "no":
        print("Restarting the process...")
        continue  # Restart the loop if they do not want to proceed
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

        