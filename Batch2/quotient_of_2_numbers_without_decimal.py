#Program 4 Batch 2
#Atienza,Rein Gabriel
#BSCPE 1-2
def quotient_of_the_2_numbers_without_decimal():
    """prompts the user to enter 2 numbers and then divides them with each other to get the quotient without the decimal"""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    quotient = num1 / num2

    print("the quotient of 2 numbers is:",int(quotient) )

quotient_of_the_2_numbers_without_decimal()