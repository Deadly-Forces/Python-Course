# Shopping Cart Program
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nTotal: ${total:.2f}")
