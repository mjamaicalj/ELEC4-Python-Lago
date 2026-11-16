
# Activity P2 - Custom Module: student_utils
# Main Program - Student Grade Report

import student_utils
from student_utils import get_highest_grade, get_lowest_grade



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

if __name__ == "__main__":
    student_grades = enter_grades()

    average = student_utils.calculate_average(student_grades)
    status = student_utils.check_pass_fail(average)
    highest = get_highest_grade(student_grades)
    lowest = get_lowest_grade(student_grades)

    print("\n================================")
    print("       STUDENT GRADE REPORT          ")
    print("================================")
    print(f"Provided Grades: {student_grades}")
    print(f"Average Grade  : {average:.2f}")
    print(f"Grade Status   : {status}")
    print(f"Highest Grade  : {highest:.2f}")
    print(f"Lowest Grade   : {lowest:.2f}")
    print("================================")