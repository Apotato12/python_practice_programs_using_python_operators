#Program 7 Batch 2
#Atienza,Rein Gabriel
#BSCPE 1-2
def even_numbers_within_10_inputs():
    """"Prompts the user to enter 10 numbers then check which are the even numbers then prints them"""
    numbers = [0] * 10

    for i in range(10):
        numbers[i] = float(input(f"Enter number {i + 1}: "))

    even_numbers = [num for num in numbers if num % 2 == 0]

    print("Count of even numbers:", even_numbers)

even_numbers_within_10_inputs()