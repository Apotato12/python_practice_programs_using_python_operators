highest_number = set()

while True:
        user_input = input("Enter a number (or type something invalid to stop): ")
        
        try:
            num = float(user_input)  # Convert input to float
            highest_number.add(num)  # Add the number to the set
        except ValueError:
            print("Invalid input. Exiting the program.")
            break
        
if highest_number:
        highest_number = max(highest_number)
        print("The highest number entered is:", highest_number)
else:
        print("No valid highest_number were entered.")