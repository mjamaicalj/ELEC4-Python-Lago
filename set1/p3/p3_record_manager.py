
# Activity: P3 - Student Record Manager
# Commit 2: Add Students and Prevent Duplicates

# List for storing student names
students = []

# Set for preventing duplicate names
student_names = set()


# Function to add a student
def add_student():
    name = " ".join(input("Enter student name: ").split())

    if not name:
        print("Student name cannot be empty!")
        return

    name_key = name.casefold()

    if name_key in student_names:
        print("Student already exists! Prevent duplicate entry.")
    else:
        students.append(name)
        student_names.add(name_key)
        print(f"Student '{name}'successfully added!")


# Function to display all students
def display_students():
    print("\n===== STUDENT PROFILES=====")

    if len(students) == 0:
        print("No students found.")
    else:
        sorted_students = sorted(students, key=str.casefold)

        for number, name in enumerate(sorted_students, start=1):
            print(f"{number}. {name}")

    print(f"Total Students: {len(students)}")


# Main menu function
def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Exit")

        choice = input("Enter your number choice (1-3): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            print("Thank you for using Student Record Manager!")
            break

        else:
            print("Not in the choice. Please try again.")


if __name__ == "__main__":
    main()
