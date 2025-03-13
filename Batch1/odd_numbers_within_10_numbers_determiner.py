#Program 8
#Atienza,Rein Gabriel
#BSCPE 1-2
""""starts the value of odss to 0 to hold the other values given and then adds 1 to it when and odd number is"""
def Odd_numbers_within_10():

    odd_numbers = 0

    for i in range(10):
        number = float(input(f"Enter number {i + 1}: ")) 
    
        if number % 2 != 0:
            odd_numbers += 1 

    print("The number of odd numbers entered is:", odd_numbers)

Odd_numbers_within_10()