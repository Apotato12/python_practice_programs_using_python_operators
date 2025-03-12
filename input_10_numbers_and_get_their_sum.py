sum = 0

for i in range(10):
    number = float(input(f"Enter number {i + 1}: "))  # Prompt for each number
    sum += number  # Add the number to the total sum

# Print the sum of all the numbers
print(f"The sum of all the numbers is:", sum)