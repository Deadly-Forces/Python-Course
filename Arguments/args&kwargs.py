def shipping_lable(*args, **kwargs):
    for args in args:
        print(args, end=" ")
    print()    
    for value in kwargs.values():
        print(value, end=" ")

shipping_lable("Nikunj", "Kaslikar", 
               street="123 Saint St.", 
               city="Detroit", 
               state="MI", 
               zipcode="54321")
# Compare this snippet from Arguments/args%26kwargs.py: