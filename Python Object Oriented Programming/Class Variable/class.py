# class variables = Shared among all instances of a class
#                   Defined outside the contructor
#                   Allows you to share data among all objects created from that class.

class student:

    class_year = 2027
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.num_students += 1

student1 = student("Spongebob", 30)
student2 = student("Patrick", 35)
student3 = student("Sandy", 25)
student4 = student("Squidward", 40)
"""print(student1.name)
print(student2.name)
print(student1.age)
print(student2.age)
print(student1.class_year)
print(student2.class_year)
print(student.num_students)"""
print(f"My graduating class of {student.class_year} has {student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)