# Python Banking Problem

def show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: "))
    if amount < 0:
        print("Invalid amount. Please enter a positive number.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
    return balance

balance = 0
is_running = True

while is_running:
    print("Welcome to the Bank")
    show_balance(balance)
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        show_balance(balance)
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance = withdraw(balance)
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice. Please try again.")