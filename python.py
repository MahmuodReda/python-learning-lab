#!/usr/bin/python
# Example: Using OOP to manage students in a simple way

class Student:
    # Constructor: initializes the student data
    def __init__(self, name, age, grades):
        self.name = name        # store student's name
        self.age = age          # store student's age
        self.grades = grades    # store list of grades

    # Method: print student info with average grade
    def print_info(self):
        avg = sum(self.grades) / len(self.grades)
        print(f"Name: {self.name}, Age: {self.age}, Average Grade: {avg:.2f}")

    # Method: add a new grade
    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Added grade {grade} for {self.name}")

    # Method: check if student passed (average >= 60)
    def has_passed(self):
        avg = sum(self.grades) / len(self.grades)
        return avg >= 60


# Create student objects
student1 = Student("Ahmed", 20, [90, 85, 88])
student2 = Student("Mona", 22, [55, 60, 58])

# Print their info
student1.print_info()
student2.print_info()

# Add a new grade to Ahmed
student1.add_grade(95)
student1.print_info()

# Check pass/fail status
print(f"Did {student1.name} pass? {student1.has_passed()}")
print(f"Did {student2.name} pass? {student2.has_passed()}")


