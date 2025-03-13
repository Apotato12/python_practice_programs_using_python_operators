# Program 3 Batch 2
# Atienza, Rein Gabriel
# BSCPE 1-2
def track_numbers():
    """Continuously ask the user for a number and track unique and duplicate entries."""
    duplicate_numbers = set()
    unique_numbers = set()

    while True:
        user_input = input("Enter a number (or type something invalid to stop): ")
        
        try:
            num = float(user_input) 
            if num in unique_numbers:
                duplicate_numbers.add(num)
            else:
                unique_numbers.add(num)
        except ValueError:
            print("Invalid input. Exiting the program.")
            break

    print("Unique numbers entered:")
    for number in unique_numbers:
        print(number)

    print("Duplicate numbers entered:")
    for number in duplicate_numbers:
        print(number)

track_numbers()