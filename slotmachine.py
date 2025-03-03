# Python Slot Machine
import random

def spin_row():
    symbols = ["🍒", "💰", "🍊", "🍇", "🍉", "🍌"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************************")
    print(" | ".join(row))
    print("*************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        payout = bet * 3
        print(f"Congratulations! You won ${payout}!")
    elif row[0] == row[1] or row[0] == row[2] or row[1] == row[2]:
        payout = bet * 2
        print(f"Congratulations! You won ${payout}!")
    else:
        print("Sorry, you lost.")
        payout = 0
    return payout

def main():
    balance = 100
    print("Welcome to the Python Slot Machine!")
    print("Symbols: 🍒  💰  🍊  🍇  🍉  🍌")

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Enter your bet: ")
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue
        bet = int(bet)
        if bet > balance:
            print("You don't have enough money to make that bet.")
            continue
        if bet<=0:
            print("Bet Must be greater than 0.")
            continue    
        balance -= bet
        row = spin_row()
        print_row(row)
        print("Spinning...\n")
        payout = get_payout(row, bet)
        if payout > 0:
            balance += payout
if __name__ == "__main__":
    main()