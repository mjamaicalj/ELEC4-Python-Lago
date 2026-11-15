
# Activity: P3 - Student Record Manager
# Commit 1: Basic Student Record Manager Menu

# List for storing student names
students = []


# Function to display all students
def display_students():
    print("\n===== STUDENT RECORDS =====")

    if len(students) == 0:
        print("No students found.")
    else:
        sorted_students = sorted(students, key=str.lower)

        for number, name in enumerate(sorted_students, start=1):
            print(f"{number}. {name}")

    print(f"Total Students: {len(students)}")


# Main menu function
def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Display All Students")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            display_students()

        elif choice == "2":
            print("Thank you for using Student Record Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
