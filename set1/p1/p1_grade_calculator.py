# Name: Ma. Jamaica LJ J. Lago
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 15, 2026


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


def display_results(grades):
    if not grades:
        print("\nNo grades entered yet.")
        return

    print("\n===== GRADE EVALUATION =====")
    print("Student: Ma. Jamaica LJ J. Lago")
    print(f"Overall Grade: {calculate_average(grades):.2f}")
    print(f"Top Grade: {highest_grade(grades):.2f}")
    print(f"Lowest Grade: {lowest_grade(grades):.2f}")
    print(f"Grade Status: {check_status(grades)}")


def main():
    grades = []

    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            grades = enter_grades()
            print("\nGrades recorded successfully.")

        elif choice == "2":
            display_results(grades)

        elif choice == "3":
            print("\nProgram closed.")
            break

        else:
            print("\nInvalid option. Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()


# A local variable is created inside a function and can only be used within that function.
# In my program, grades is a local variable in main() that stores the grades entered by the user.
# A global variable is declared outside functions and can be accessed by different functions in the program.
# I used local variables to keep the student grades organized and avoid unnecessary changes.
# Instead of using a global variable, I passed grades to other functions to calculate and display the results.