# dictionary is a collection of key-value pairs

capitals = {'USA': 'Washington, D.C.', 
            'France': 'Paris', 
            'India': 'New Delhi'}


# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
#if capitals.get("Japan"):
#    print("That capital in the dictionary")
#else:
#    print("That capital is not in the dictionary")
# capitals.update({"Germany": "Berlin"})
# print(capitals)
# capitals.pop("USA")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#    print(key)

# values = capitals.values()
# for value in capitals.values():
#    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")