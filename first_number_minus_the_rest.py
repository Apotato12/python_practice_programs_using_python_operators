#Program 6 Batch 2
#Atienza,Rein Gabriel
#BSCPE 1-2
def first_minus_the_rest():
    """"ask the user to input 10 numbers then seperate the first numbers with the other then get the difference"""
    numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(10)]

    first_number = numbers[0]
    rest_of_numbers = numbers[1:]

    result = first_number - sum(rest_of_numbers)

    print("Result:", result)

first_minus_the_rest()