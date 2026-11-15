
# Activity P2 - Custom Module: student_utils
# Main Program - Student Grade Report


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
                choice = input("Add another grade? (Y/N): ").strip().lower()

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
    print("Grades entered:", student_grades)
