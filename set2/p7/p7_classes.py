# Full name: Ma. Jamaica LJ J. Lago
# Section: IV BSIT-A
# Activity: P7 - Student Management System with Classes
# Date: November 22, 2026


class Student:
    def __init__(self, student_id, full_name, grade):
        self.student_id = student_id
        self.full_name = full_name
        self.set_grade(grade)

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        # Check the grade before assigning it to the private attribute.
        if type(grade) not in (int, float) or not 0 <= grade <= 100:
            raise ValueError("Grade must be a number from 0 to 100.")

        self.__grade = grade

    def update_info(self, full_name, grade):
        self.set_grade(grade)
        self.full_name = full_name

    def display_info(self):
        print(f"{self.student_id} | {self.full_name} | {self.get_grade():.2f}")


class Subject:
    def __init__(self, code, title):
        self.code = code
        self.title = title


class Section:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"\nSection: {self.name}")
        print(f"Subject: {self.subject.code} - {self.subject.title}")
        print("\nID | Full name | Grade")

        for student in self.students:
            student.display_info()


if __name__ == "__main__":
    print("\nP7 - Student Management System")
    print("Prepared by: Ma. Jamaica LJ J. Lago")

    subject = Subject("ELEC 4", "Python Programming")
    section = Section("IV BSIT A", subject)

    student = Student("S-001", "Ana Reyes", 91)
    section.enroll_student(student)
    section.display_students()