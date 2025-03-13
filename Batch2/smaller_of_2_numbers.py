#Program 1 batch 2
#Atienza,Rein Gabriel
#BSCPE 1-2
def determine_smaller_number():
    """Ask the user to input 2 numbers and determine which one is smaller."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if num1 < num2:
        print(num1, "is the smaller number")
    elif num2 < num1:
        print(num2, "is the smaller number")
    else:
        print("No number is smaller than the other.")

determine_smaller_number()