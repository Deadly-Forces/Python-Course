def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0.1))