# Full name: Ma. Jamaica LJ J. Lago
# Section: [Your section]
# Activity: P5 - Student Information File System
# Date: [Date]

import csv
from pathlib import Path

STUDENTS_FILE = Path(__file__).with_name("students.txt")


def load_students():
    # Start with an empty list if students.txt does not exist yet.
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8", newline="") as file:
            return [row for row in csv.reader(file) if row]
    except FileNotFoundError:
        return []


def add_student(students):
    student_id = input("\nStudent ID: ").strip().upper()
    if not student_id:
        print("\nStudent ID is required.")
        return

    if any(record[0] == student_id for record in students):
        print("\nThat student ID already exists.")
        return

    full_name = input("Full name: ").strip()
    course_section = input("Course/section: ").strip()
    if not full_name or not course_section:
        print("\nFull name and course/section are required.")
        return

    try:
        average = float(input("General average (0-100): "))
    except ValueError:
        print("\nEnter a numeric general average.")
        return

    if not 0 <= average <= 100:
        print("\nGeneral average must be between 0 and 100.")
        return

    record = [student_id, full_name, course_section, f"{average:.2f}"]

    # Append one student per line.
    try:
        with open(STUDENTS_FILE, "a", encoding="utf-8", newline="") as file:
            csv.writer(file).writerow(record)
    except OSError as error:
        print(f"\nCould not save the record: {error}")
        return

    students.append(record)
    print("\nStudent record saved.")


def display_students(students):
    if not students:
        print("\nNo student records yet.")
        return

    print("\nID | Full name | Course/section | General average")
    for record in students:
        print(" | ".join(record))


def search_student(students):
    student_id = input("\nEnter Student ID to search: ").strip().upper()

    for record in students:
        if record[0] == student_id:
            print("\n===== STUDENT FOUND =====")
            print("ID | Full name | Course/section | General average")
            print(" | ".join(record))
            return

    print("\nStudent ID not found.")


def update_student(students):
    student_id = input("\nEnter Student ID to update: ").strip().upper()

    for index, record in enumerate(students):
        if record[0] == student_id:
            print("\n===== CURRENT STUDENT INFORMATION =====")
            print("ID | Full name | Course/section | General average")
            print(" | ".join(record))

            print("\n===== ENTER UPDATED INFORMATION =====")
            full_name = input("New full name: ").strip()
            course_section = input("New course/section: ").strip()

            if not full_name or not course_section:
                print("\nName and course/section cannot be empty.")
                return

            try:
                average = float(input("New general average (0-100): "))
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                return

            if not 0 <= average <= 100:
                print("\nAverage must be between 0 and 100.")
                return

            updated_record = [
                student_id,
                full_name,
                course_section,
                f"{average:.2f}"
            ]

            updated_students = students.copy()
            updated_students[index] = updated_record

            # Save the updated records to a temporary file first.
            temp_file = STUDENTS_FILE.with_suffix(".tmp")

            try:
                with open(temp_file, "w", encoding="utf-8", newline="") as file:
                    csv.writer(file).writerows(updated_students)

                temp_file.replace(STUDENTS_FILE)

            except OSError as error:
                print(f"\nError saving updated record: {error}")
                return

            students[index] = updated_record

            print("\nStudent record updated successfully!")
            print("\n===== UPDATED STUDENT INFORMATION =====")
            print("ID | Full name | Course/section | General average")
            print(" | ".join(updated_record))
            return

    print("\nStudent ID not found.")


def main():
    print("\nP5 - Student Information File System")
    print("Prepared by: Ma. Jamaica LJ J. Lago")

    try:
        students = load_students()
    except OSError as error:
        print(f"\nCould not read students.txt: {error}")
        return

    print(f"Records loaded: {len(students)}")

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student by ID")
        print("4. Update student")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            print("\nExiting Student Information File System.")
            break
        else:
            print("\nInvalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
