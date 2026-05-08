a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))
c = int(input("Please enter third number: "))

d = b**2 - 4 * a * c
x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)

print(x1, x2)