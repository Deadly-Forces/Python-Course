# Python compound intrest calculator
principle = 0
rate = 0
time = 0

while principle < 0:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount must be greater than or equal to 0")


while rate < 0:
    rate = float(input("Enter the Interest rate amount: "))
    if rate < 0:
        print("Interest Rate must be greater than 0")


while time < 0:
    time = float(input("Enter the amount of time: "))
    if time < 0:
        print("Amount of time must be greater than 0")


"""print(principle)
print(rate)
print(time)"""

total = principle * pow((1 + rate / 100),time)
print (f"Balance after {time} year/s is {total:.2f}")