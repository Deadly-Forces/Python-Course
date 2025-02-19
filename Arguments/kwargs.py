def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

print_address(street="123 Saint St.", 
              city="Detroit", 
              state="MI", 
              zipcode="54321")