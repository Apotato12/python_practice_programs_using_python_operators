#Program 8 Batch 2
#Atienza,Rein Gabriel
#BSCPE 1-2
def odd_numbers_within_100():
    """prints the odd numbers that are present from 0 to 100"""
    number = 0  
    while number <= 100:
        if number % 2 != 0:
            print(number)
        number += 1

odd_numbers_within_100()