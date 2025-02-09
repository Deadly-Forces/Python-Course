import math
"""x = 9.1
#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
result = math.floor(x)
print(result)"""


# Exercise: Program that calculates the circumference of a circle.
"""radius = float(input('Enter the radius of a circle: '))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")"""


# Exercise: Program that calculates the area of a circle.
"""radius = float(input("Enter the radius of the circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm^2")"""


# Exercise: Program that calculates the hypotenuse of a right-angled triangle.
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")