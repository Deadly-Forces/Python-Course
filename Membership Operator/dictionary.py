grades = {"Sandy": 8.5, 
          "Kenny": 7.5}

student = input("Enter the name of a student: ")
if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:
    print(f"{student} was not found")
