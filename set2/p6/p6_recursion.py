# Full name: Ma. Jamaica LJ J. Lago
# Section: [Your section]
# Activity: P6 - Recursion Toolkit
# Date: [Date]

from functools import lru_cache


# Base case: factorial(0) returns 1.
# Recursive call: factorial(n - 1).
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Base cases: fibonacci(0) returns 0 and fibonacci(1) returns 1.
# Recursive calls: fibonacci(n - 1) and fibonacci(n - 2).
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("\nP6 - Recursion Toolkit")
    print("Prepared by: Ma. Jamaica LJ J. Lago")
    print()

    print(f"Factorial of 5: {factorial(5)}")
    print(f"Fibonacci F(7): {fibonacci(7)}")

    first_terms = [fibonacci(index) for index in range(7)]
    print(f"First 7 Fibonacci terms: {first_terms}")