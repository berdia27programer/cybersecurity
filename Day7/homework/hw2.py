age = int(input("Enter your age: "))
country = int(input("Enter your country: "))

while age <= 18 and country != "Georgia":
    print("Access not granted")
    age = int(input("Enter your age: "))
    country = int(input("Enter your country: "))

print("Access granted")