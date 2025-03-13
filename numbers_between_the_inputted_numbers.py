num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    num1, num2 = num2, num1 

print("Numbers between", num1, "and", num2, ":")
for num in range(num1 + 1, num2):
    print(num)