numbers = []

for i in range(11):
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        numbers.append(f"{num} Even")
    else:
        numbers.append(f"{num} Odd")

print(numbers)        