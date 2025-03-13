# Program 1 Batch 4
# Atienza, Rein Gabriel
# BSCPE 1-2
def print_the_duplicates():
    """Ask the user to input 10 numbers and display all numbers that have duplicates."""
    numbers = set()
    duplicates = set()

    print("Enter 10 numbers:")
    for i in range(10):
        num = float(input("Number " + str(i + 1) + ": "))
     
        if num in numbers:
            duplicates.add(num)
        else:
            numbers.add(num)

    print("Numbers with duplicates:")
    for num in duplicates:
        print(num)

print_the_duplicates()