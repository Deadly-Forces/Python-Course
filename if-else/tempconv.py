unit = input("Is this temp. in Celsius or Fahrenheit? (C or F): ")
temp = float(input("Enter the temperature: "))
if unit == "C":
    temp = (temp * 9/5) + 32
    unit = "F"
    print(f"The temperature is {temp} °C.")
elif unit == "F":
    temp = (temp - 32) * 5/9
    unit = "C"
    print(f"The temperature is {temp} °F.")
else:
    print(f"{unit} is an invalid unit.")