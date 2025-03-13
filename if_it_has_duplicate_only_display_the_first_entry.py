list_of_numbers = []

for i in range(10):
    num = float(input("Number " + str(i + 1) + ": "))
    list_of_numbers.append(num)

tracker = set()
print("Numbers (duplicates shown only once):")
for num in list_of_numbers:
    if num not in tracker:
         print(num) 
         tracker.add(num)