# Program 2 Batch 2
# Atienza, Rein Gabriel
# BSCPE 1-2

def find_most_duplicate_number():
    """Ask the user to input numbers and display the number with the most duplicates."""
    number_count = {}
    unique_numbers = set()

    while True:
        user_input = input("Enter a number (or type something invalid to stop): ")
        
        try:
            num = float(user_input)
            
            if num in unique_numbers:
                number_count[num] += 1
            else:
                unique_numbers.add(num)
                number_count[num] = 1 
        except ValueError:
            print("Invalid input. Exiting the program.")
            break

    most_duplicate_number = None
    max_count = 0

    for num, count in number_count.items():
        if count > max_count:
            max_count = count
            most_duplicate_number = num

    if most_duplicate_number is not None:
        print("The number with the most duplicates is:", most_duplicate_number)
        print("It appears", max_count, "times.")
    else:
        print("No valid numbers were entered.")

find_most_duplicate_number()