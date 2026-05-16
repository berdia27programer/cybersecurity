password = "root"
balance = 0
inp = input("Enter your password: ")

while inp != password:
    print("Incorrect password, try again")
    inp = input("Enter your password: ")

while True: 
    print("Welcome to the bank")

    print("-------------------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

    select = int(input("Select options with an number from 1-4: "))

    if select == 1:
        deposit = int(input("Enter the amount of money to deposit: "))
        print("Your balance is now", balance + deposit)
    elif select == 2:
        withdraw = int(input("Enter the amount of money to withdraw: "))
        print("Your balance is now", withdraw - balance)
    elif select == 3:
        print("Your balance is", balance)
    elif select == 4:
        print("Thanks for visiting our bank")
        quit()
    else:
        print("Uknown option")