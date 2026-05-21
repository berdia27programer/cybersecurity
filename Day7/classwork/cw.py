password = "root"
inp = input("Enter your password: ")

while inp != password:
    print("Incorrect password, try again")
    inp = input("Enter your password: ")

print("Successfull login!")