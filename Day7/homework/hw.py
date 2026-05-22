start = int(input("Enter the starting number: "))
end = int(input("Enter the number it going to end: "))
step = int(input("Enter the stepping number: "))

for i in range(start, end + 1, step):
    print(i)