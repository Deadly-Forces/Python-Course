# logical operators = evaluate multiple conditions (or, and, not)
#                   = or = either condition is true
#                   = and = both conditions are true                           
#                   = not = reverse the result, returns False if the result is true

unit = input("Is this temp. in Celsius or Fahrenheit? (C or F): ")
temp = float(input("Enter the temperature: "))
"""
# Example 1 (or)
temp = 40
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The weather is bad")
else:
    print("The weather is good")

# Example 2 (and)
temp = -10
is_sunny = True
if temp >= 28 and is_sunny:
    print("The weather is Hot 🥵")
elif temp <= 0 and is_sunny:
    print("The weather is cold ❄️")
elif 28 > temp > 0 and is_sunny:
    print("The weather is warm 🌞")"""

# Example 3 (not)
if temp>=25:
    print("The weather is Hot 🥵")
is_sunny = True
if not is_sunny:
    print("The weather is cold ❄️")
else:
    print("The weather is OK")
