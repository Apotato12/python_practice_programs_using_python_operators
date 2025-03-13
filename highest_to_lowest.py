highest_to_lowest = set() 

while True:
        user_input = input("Enter a number (or type something invalid to stop): ")
        
        try:
            num = float(user_input)
            highest_to_lowest.add(num)
        except ValueError:
            print("Invalid input. Exiting the program.")
            break


if highest_to_lowest:  
        sorted_highest_to_lowest = sorted(highest_to_lowest, reverse=True)
        print("")
        for number in sorted_highest_to_lowest:
            print(number)