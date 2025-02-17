# while loop = execute some code WHILE some condition remains true
name = input("Enter your name: ")

while name == "":
    print("You must enter a name")
    name = input("Enter your name: ")
else:
    print(f"Hello, {name}")
    print("Welcome to the program")
