#Program 5 batch 2
#Atienza,Rein Gabriel
#BSCPE 1-2
def calculate_remainder():
    """Ask the user to input 2 numbers then divide the first number with the second number then print the remainder"""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    remainder = num1 % num2

    print ("the remainder is:", remainder)\

calculate_remainder()