# Full name: Ma. Jamaica LJ J. Lago
# Section: IV BSIT A
# Activity: P5 - Student Information File System
# Date: November 22, 2026

import csv
from pathlib import Path

STUDENTS_FILE = Path(__file__).with_name("students.txt")


def load_students():
    # On the first run, students.txt may not exist yet.
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8", newline="") as file:
            return [row for row in csv.reader(file) if row]
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    students = load_students()
    print("P5 - Student Information File System")
    print("Prepared by: Ma. Jamaica LJ J. Lago")
    print(f"Records loaded: {len(students)}")