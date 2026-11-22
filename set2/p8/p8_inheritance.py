# Full name: Ma. Jamaica LJ J. Lago
# Section: IV BSIT-A
# Activity: P8 - Inheritance and Polymorphism
# Date: November 22, 2026


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


if __name__ == "__main__":
    print("\nP8 - Inheritance and Polymorphism")
    print("Prepared by: Ma. Jamaica LJ J. Lago")

    student = Student("Ana Reyes", 21, "BS Information Technology")
    teacher = Teacher("Paolo Lim", 32, "Python Programming")

    print("\nStudent")
    print(student.introduce())
    print(f"Course: {student.course}")

    print("\nTeacher")
    print(teacher.introduce())
    print(f"Subject: {teacher.subject}")