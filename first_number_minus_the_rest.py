numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(10)]

first_number = numbers[0]
rest_of_numbers = numbers[1:]

result = first_number - sum(rest_of_numbers)

print("Result:", result)