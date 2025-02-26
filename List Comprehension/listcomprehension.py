# List comprehension = A concise way to create a list in python
# Compact and easier to read than traditional loops
# Syntax: list = [expression for value in iterable if condition]

#doubles = []
#for x in range(1, 6):
#    doubles.append(x * 2)
#print(doubles)    

doubles = [x * 2 for x in range(1, 6)]
triples = [y * 3 for y in range(1, 6)]
squares = [z * z for z in range(1, 6)]
print(triples)


