# Membership operators = used to test whether a value or variable is in a sequence 
# (string, list, tuple, set, dictionary)
# in
# not in

word = "Apple"

letter = input("Guess a letter in secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"There is no {letter}")    