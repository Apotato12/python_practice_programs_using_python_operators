list_of_numbers = []

print("enter 10 numbers:")
for i in range(10):
    num = float(input("Number " + str(i + 1)+ ": "))
    list_of_numbers.append(num)

count = {}
for num in list_of_numbers:
    if num in count:
        count[num] = count[num] + 1 
    else:
        count[num] = 1

print("Numbers without duplicates:")
for num in count:
    if count[num] == 1:
        print(num)
        