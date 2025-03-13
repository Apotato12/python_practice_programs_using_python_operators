# Program 10 Batch 2
# Atienza, Rein Gabriel
# BSCPE 1-2

def print_numbers_between():
    """Ask the user for 2 numbers and print all numbers between them."""
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num1 > num2:
        num1, num2 = num2, num1 

    print("Numbers between", num1, "and", num2, ":")
    for num in range(num1 + 1, num2):
        print(num)

print_numbers_between()