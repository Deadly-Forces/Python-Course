# *args    =allows you to pass multiple non-key arguments
# **kwargs  =allows you to pass multiple keyword arguments
#            * unpacking operator
#            1. positional, 2. default, 3. keywords, 4. arbitrary

# *args
#def add(*args):
#    total = 0
#    for arg in args:
#        total += arg
#    return total

#print(add(1, 2, 3))

def display_name(*args):
    for args in args:
        print(args, end=" ")

display_name("Mr.", "Nikunj", "Kaslikar")