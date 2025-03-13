numbers = set()
duplicates = set()

print("Enter 10 numbers:")
for i in range(10):
     num = float(input("Number " + str(i + 1) + ": "))
     
     if num in numbers:
            duplicates.add(num)
     else:
            numbers.add(num)

print("Numbers with duplicates:")
for num in duplicates:
    print(num)