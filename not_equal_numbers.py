#Program 2 Batch 2
#Atienza,Rein Gabriel
#BSCPE 1-2
def determine_if_numbers_are_not_equal():
    """Ask the user for 2 numbers and determine if they are equal or not."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if num1 != num2:
        print("The numbers are not equal.")
    else:
        print("The numbers are equal.")

determine_if_numbers_are_not_equal()