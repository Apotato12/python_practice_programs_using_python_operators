#Program 10
#Atienza,Rein Gabriel
#BSCPE 1-2
def every_number_in_100_without_zero():
    """"Prints the values in 0 to 100 but without the numbers ending in 0"""
    for number in range(101):
        
        if number % 10 != 0:

            print(number)  \

every_number_in_100_without_zero()