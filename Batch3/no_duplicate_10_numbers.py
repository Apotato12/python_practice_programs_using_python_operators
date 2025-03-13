# Program 1 Batch 3
# Atienza, Rein Gabriel
# BSCPE 1-2
def find_non_repeating_numbers():
    """Ask the user to input 10 numbers and display those without duplicates."""
    list_of_numbers = []

    print("Enter 10 numbers:")
    for i in range(10):
        num = float(input("Number " + str(i + 1) + ": "))
        list_of_numbers.append(num)

    count = {}
    for num in list_of_numbers:
        if num in count:
            count[num] = count[num] + 1 
        else:
            count[num] = 1

    print("Numbers without duplicates:")
    for num in count:
        if count[num] == 1:
            print(num)

find_non_repeating_numbers()