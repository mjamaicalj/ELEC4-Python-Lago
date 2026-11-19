# Name: Ma. Jamaica LJ J. Lago
# Section: IV-BSIT A
# Activity: P2 - Custom Module: student_utils
# Date: November 19, 2026
# Main Program - Student Grade Report

import student_utils
from student_utils import get_highest_grade, get_lowest_grade
from datetime import datetime


def enter_grades():
    grades = []

    while True:
        try:
            grade = float(input("Enter grade (0-100): "))

            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Invalid grade! Enter 0 to 100.")
                continue

            while True:
                choice = input("You want to add another grade? (Y/N): ").strip().lower()

                if choice in ("y", "n"):
                    break

                print("Invalid choice! Enter Y or N.")

            if choice == "n":
                break

        except ValueError:
            print("Invalid input! Numbers only.")

    return grades


def display_report(grades):
    average = student_utils.calculate_average(grades)
    status = student_utils.check_pass_fail(average)
    highest = get_highest_grade(grades)
    lowest = get_lowest_grade(grades)

    date_generated = datetime.now().strftime("%B %d, %Y - %I:%M:%S %p")

    print("\n================================")
    print("       STUDENT GRADE REPORT")
    print("================================")
    print("Student: Ma. Jamaica LJ J. Lago")
    print(f"Provided Grades: {grades}")
    print(f"Average Grade  : {average:.2f}")
    print(f"Grade Status   : {status}")
    print(f"Highest Grade  : {highest:.2f}")
    print(f"Lowest Grade   : {lowest:.2f}")
    print(f"Report Generated: {date_generated}")
    print("================================")


if __name__ == "__main__":
    student_grades = enter_grades()
    display_report(student_grades)