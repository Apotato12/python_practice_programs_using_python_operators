#Program 6
#Atienza,Rein Gabriel
#BSCPE 1-2
def raise_num1_to_num2():
    """"prompts the user to enter 2 numbers after entering 2 numbers raise num 1 with num 2"""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    raised = num1 ** num2

    print ("num1 raised to num 2 is", raised)

raise_num1_to_num2()