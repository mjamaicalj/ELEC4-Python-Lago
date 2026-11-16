
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
        print(f"Student '{name}' successfully added!")


# Function to remove a student
def remove_student():
    name = " ".join(input("Enter student name to remove: ").split())

    if not name:
        print("Please enter a student name to remove.")
        return

    name_key = name.casefold()

    if name_key not in student_names:
        print("Student not found!")
        return

    for student in students:
        if student.casefold() == name_key:
            students.remove(student)
            student_names.remove(name_key)
            print(f"Student '{student}' successfully removed!")
            return



# Function to search for a student
def search_student():
    search = " ".join(input("Enter student name to search: ").split()).casefold()

    if not search:
        print("Please enter a student name to search.")
        return

    matches = []

    for name in students:
        if search in name.casefold():
            matches.append(name)

    print("\n===== SEARCH RESULTS =====")

    if len(matches) == 0:
        print("No matching students found.")
    else:
        sorted_matches = sorted(matches, key=str.casefold)

        for number, name in enumerate(sorted_matches, start=1):
            print(f"{number}. {name}")

    print(f"Total Matches: {len(matches)}")



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
        print("2. Search Student")
        print("3. Remove Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your number choice (1-5): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            search_student()

        elif choice == "3":
            remove_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break

        else:
            print("Not in the choice. Please try again.")


if __name__ == "__main__":
    main()


# A list is an ordered collection that allows duplicate values.
# A set is an unordered collection that stores only unique values.
# In this program, I used a list to store and display student names.
# I used a set to prevent duplicate names regardless of capitalization.
# Both collections help manage student records efficiently.

