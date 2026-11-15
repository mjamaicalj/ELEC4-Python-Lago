#Name: Ma. Jamaica LJ J. Lago
#Section: IV-BSIT A
#Activity: P1 - Student Grade Calculator
#Date: November 15, 2026

def enter_grades():
    grades = []

    while True:
        try:
            count = int(input("Number of Grades:  "))

            if count > 0:
                break
            else:
                print("Provide at least one grade.")

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


student_grades = enter_grades()
print("\nGrades entered:", student_grades)
