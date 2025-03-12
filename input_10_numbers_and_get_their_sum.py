#Program 7
#Atienza,Rein Gabriel
#BSCPE 1-2
def get_10_numbers_and_their_sum():
    """"starts the value of sum to 0 to hold the other values given and then adds them with each other"""
    sum = 0

    for i in range(10):
        number = float(input(f"Enter number {i + 1}: "))  # Prompt for each number
        sum += number  # Add the number to the total sum

        print(f"The sum of all the numbers is:", sum)

get_10_numbers_and_their_sum()