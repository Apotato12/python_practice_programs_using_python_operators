odd_count = 0

for i in range(10):
    number = float(input(f"Enter number {i + 1}: ")) 
    
    if number % 2 != 0:
        odd_count += 1 

print(f"The number of odd numbers entered is: {odd_count}")