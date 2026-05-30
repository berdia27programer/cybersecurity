numbers = []

for i in range(6):
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        numbers.append(num * num)
    else:
        numbers.append(num)

print(numbers)        