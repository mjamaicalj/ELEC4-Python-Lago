#Name: Ma. Jamaica LJ J. Lago
#Section: IV-BSIT A
#Activity: P1 - Student Grade Calculator
#Date: November 15, 2026


def enter_grades():
    grades = []

    while True:
        try:
            count = int(input("Number of Grades: "))

            if count > 0:
                break
            else:
                print("Please enter at least one grade.")

        except ValueError:
            print("Invalid input. Enter a whole number.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Provide grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please try again.")

    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def highest_grade(grades):
    return max(grades)


def lowest_grade(grades):
    return min(grades)


def check_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASS"
    else:
        return "FAIL"


student_grades = enter_grades()

print("\n--- STUDENT GRADE PREVIEW---")
print(f"Overall Grade: {calculate_average(student_grades):.2f}")
print(f"Top Grade: {highest_grade(student_grades):.2f}")
print(f"Lowest Grade: {lowest_grade(student_grades):.2f}")
print(f"Grade Status: {check_status(student_grades)}")

