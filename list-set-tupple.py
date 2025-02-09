# collection = single "variable" that holds multiple values
#   list = [] ordered and changable. Duplicates OK
#   Set = {} unorderd and immutable, but Add/Remove OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. Faster

#Lists
# fruits = ["apple", "banana", "cherry", "melon", "mango"]
# print(dir(fruits))
# print(help(fruits))
# print(fruits[0:3])
# for x in fruits:
#    print(x)

# len operator
#print(len(fruits))

# in operator
#print("apple" in fruits)
#print("pear" in fruits)

#fruits[1] = "pear"
#for fruit in fruits:
#    print(fruits)

# To add an item to the end of the list, use the append() method
# fruits.append("pear")
# print(fruits)

#To remove an item from the list, use the remove() method
# fruits.remove("pear")
# print(fruits)

#To insert an item at a specified index, use the insert() method
# fruits.insert(0, "pear")
# print(fruits)

# To sort the list in ascending order, use the sort() method
# fruits.sort()
# print(fruits)

# To reverse the order of the list, use the reverse() method
# fruits.reverse()
# print(fruits)

# To clear the list, use the clear() method
# fruits.clear()
# print(fruits)

# To index the list, use the index() method
# print(fruits.index("cherry"))
# print(fruits)

# To count the number of times an item appears in the list, use the count() method
# print(fruits.count("apple"))
# print(fruits)

# SETS

#fruits = {"apple", "banana", "cherry", "melon", "mango"}
#fruits.add("pear")
#fruits.remove("pear")
#fruits.pop()
#fruits.clear()
#print(fruits)

#Tuples

fruits = ("apple", "banana", "cherry", "melon", "mango")
print(fruits.index("cherry"))
print(fruits.count("apple"))

for x in fruits:
    print(x)

