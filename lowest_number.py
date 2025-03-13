lowest_numbers = set()

while True:
        user_input = input("Enter a number (or type something invalid to stop): ")
        try:
            num = float(user_input)
            lowest_numbers.add(num)
        except ValueError:
            print("Invalid input. Exiting the program.")
            break
if lowest_numbers:
        lowest_number = min(lowest_numbers) 
        print("The lowest number entered is:", lowest_number)
else:
        print("No valid numbers were entered.")