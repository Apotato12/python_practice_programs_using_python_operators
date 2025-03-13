# Program 9 Batch 2
# Atienza, Rein Gabriel
# BSCPE 1-2

def numbers_ending_with_0_or_5():
    """Print numbers from 0 to 100 that end with 0 or 5."""
    for number in range(101):
        if number % 10 == 0 or number % 10 == 5:
            print(number)

numbers_ending_with_0_or_5()