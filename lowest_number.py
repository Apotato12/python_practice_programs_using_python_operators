# Program 4 Batch 3
# Atienza, Rein Gabriel
# BSCPE 1-2
def find_lowest_number():
    lowest_numbers = set()

    while True:
        """Ask the user to input numbers, store them in a set, and print the lowest number."""
        user_input = input("Enter a number (or type something invalid to stop): ")
        try:
            num = float(user_input)
            lowest_numbers.add(num)
        except ValueError:
            print("Invalid input. Exiting the program.")
            break
    if lowest_numbers:
        lowest_number = min(lowest_numbers) 
        print("The lowest number entered is:", lowest_number)
    else:
        print("No valid numbers were entered.")

find_lowest_number()
