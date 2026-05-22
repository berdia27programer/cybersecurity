num = int(input("Enter a number: "))

for i in range(num + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)