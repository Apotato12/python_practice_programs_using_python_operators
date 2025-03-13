numbers = set()

while True:
    user_input = input("Enter a number (or type something invalid to stop): ")
        
    try:
        num = float(user_input)
        numbers.add(num)
    except ValueError:
        print("Invalid input. Exiting the program.")
        break

if numbers:  
    average = sum(numbers) / len(numbers) 
    print("The average of the entered numbers is:", average)