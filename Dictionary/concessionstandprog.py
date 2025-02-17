# Concession stand program
# dictionary {key:value}

menu = {"pizza": 3.00,
        "hotdog": 2.00,
        "soda": 1.00,
        "popcorn": 1.50,
        "candy": 1.75,
        "soda": 1.00}
cart = []
total = 0
print("----------Menu----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Enter an item to add to your cart(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)   
print(total)