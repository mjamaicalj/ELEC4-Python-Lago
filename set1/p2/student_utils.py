# Name: Ma. Jamaica LJ J. Lago
# Section: IV-BSIT A
# Activity: P2 - Custom Module: student_utils
# Date: November 19, 2026
# Description: Reusable functions for student grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def check_pass_fail(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)