numbers = set()
while True:
        user_input = input("Enter a number (or type something invalid to stop): ")
        try:
            num = float(user_input)
            numbers.add(num)
        except ValueError:
            print("Invalid input. Exiting the program.")
            break

sorted_numbers = sorted(numbers)

print("Numbers from lowest to highest:")
for number in sorted_numbers:
    print(number)