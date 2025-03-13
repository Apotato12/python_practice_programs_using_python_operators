# Program 4 Batch 4
# Atienza, Rein Gabriel
# BSCPE 1-2

def sort_numbers_highest_to_lowest():
    """Prompt the user to input numbers and display them from highest to lowest."""
    highest_to_lowest = set()

    while True:
        user_input = input("Enter a number (or type something invalid to stop): ")
        
        try:
            num = float(user_input)
            highest_to_lowest.add(num) 
        except ValueError:
            print("Invalid input. Exiting the program.")
            break

    if highest_to_lowest:  
        sorted_highest_to_lowest = sorted(highest_to_lowest, reverse=True)
        print("\nNumbers from highest to lowest:")
        for number in sorted_highest_to_lowest:
            print(number)
    else:
        print("No valid numbers were entered.")

sort_numbers_highest_to_lowest()