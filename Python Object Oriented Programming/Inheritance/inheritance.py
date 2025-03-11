# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

class Mouse(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Mouse")
        self.breed = breed

dog = Dog("Max", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")
mouse = Mouse.name("Jerry", "Mouse")

print(dog.name)
print(dog.breed)
print(cat.name)
print(cat.breed)

