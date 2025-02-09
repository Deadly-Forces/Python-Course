# Weight Convertor Program

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {weight} {unit}.")
else:
    print(f"{unit} is invalid unit")
