# Program 2 Batch 3
# Atienza, Rein Gabriel
# BSCPE 1-2
def display_unique_numbers():
    """Ask the user to input 10 numbers and display each number show the duplicates only once."""
    list_of_numbers = []

    print("Enter 10 numbers:")
    for i in range(10):
        num = float(input("Number " + str(i + 1) + ": "))
        list_of_numbers.append(num)

    tracker = set()
    print("Numbers (duplicates shown only once):")
    for num in list_of_numbers:
        if num not in tracker:
            print(num)  
            tracker.add(num)  

display_unique_numbers()