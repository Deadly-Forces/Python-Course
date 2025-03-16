# super() = Function used in a child class to call meathods from the parent class (superclass)
#           Allows you to extend the functionality of the inherited meathod 
class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.filled = is_filled

    def describe(self):
        return f"Shape color: {self.color} and {self.filled}"
class Circle(Shapes):
    def __init__(self, color, radius, is_filled,):
        super().__init__(color, is_filled)
        self.radius = radius
        

class Square(Shapes):
    def __init__(self, color, width, is_filled):
        super().__init__(color, is_filled)
        self.side = width
        


class Triangle(Shapes):
    def __init__(self, color, width, height, is_filled):
        super().__init__(color, is_filled)
        self.base = width
        self.height = height
        
circle = Circle("red", 5, True)
square = Square("blue", 10, False)
triangle = Triangle("green", 10, 20, True)
print(circle.color)
print(circle.radius)
print(circle.filled)
print(circle.describe())
print(square.describe())
print(square.color)
print(square.side)  
print(square.filled)
print(triangle.describe())
print(triangle.color)
print(triangle.base)
print(triangle.height)
print(triangle.filled)