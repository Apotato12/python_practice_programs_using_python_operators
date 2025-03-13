# Program 3 Batch 4
# Atienza, Rein Gabriel
# BSCPE 1-2

def find_highest_number():
    """Prompt the user to input numbers and display the highest number entered."""
    highest_numbers = set() 

    while True:
        user_input = input("Enter a number (or type something invalid to stop): ")
        
        try:
            num = float(user_input)
            highest_numbers.add(num)
        except ValueError:
            print("Invalid input. Exiting the program.")
            break

    if highest_numbers:
        highest_number = max(highest_numbers) 
        print("The highest number entered is:", highest_number)
    else:
        print("No valid numbers were entered.")

find_highest_number()