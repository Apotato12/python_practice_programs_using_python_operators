numbers = [0] * 10

for i in range(10):
    numbers[i] = float(input(f"Enter number {i + 1}: "))

even_numbers = [num for num in numbers if num % 2 == 0]

print("Count of even numbers:", even_numbers)