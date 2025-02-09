#conditional expression = A one line shortcut for the if-else statement (ternary operator)
#                         Print or assign one of two values based on a condition
#                         X if (condition) else Y

# num = 5
#a= 6
#b= 7
#age = 25
#temperature = 20
user_role = "guest"
# print("Positive" if num > 0 else "Negative") # Positive
# result = "Even" if num % 2 == 0 else "Odd"
# max_num = a if a > b else b
# print(max_num)
# min_num = a if a < b else b
# print(min_num)
# status = "Adult" if age >= 18 else "Minor"
# print(status)
# weather = "Warm" if temperature > 20 else "Cold"
# print(weather)
access_level = "Full Access" if user_role == "admin" else "Restricted Access"
print(access_level) # Restricted Access