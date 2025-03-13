# Program 5 Batch 4
# Atienza, Rein Gabriel
# BSCPE 1-2

def calculate_average():
    """Prompt the user to input numbers and display the average of those numbers."""
    average_numbers = set()

    while True:
        user_input = input("Enter a number (or type something invalid to stop): ")
        
        try:
            num = float(user_input)
            average_numbers.add(num)
        except ValueError:
            print("Invalid input. Exiting the program.")
            break

    if average_numbers:  
        average = sum(average_numbers) / len(average_numbers)
        print("The average of the entered numbers is:", average)
        
calculate_average()