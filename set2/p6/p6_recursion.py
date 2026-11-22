# Full name: Ma. Jamaica LJ J. Lago
# Section: IV BSIT-A
# Activity: P6 - Recursion Toolkit
# Date: November 22, 2026

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


# Base case: sum_numbers(0) returns 0.
# Recursive call: sum_numbers(n - 1).
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base cases: an empty list returns False, and a matching first item returns True.
# Recursive call: search(items[1:], target).
def search(items, target):
    if not items:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def main():
    print("\nP6 - Recursion Toolkit")
    print("Prepared by: Ma. Jamaica LJ J. Lago")

    while True:
        print("\n1. Factorial")
        print("2. Fibonacci")
        print("3. Sum from 1 to n")
        print("4. Search a list")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "5":
            break
        if choice not in {"1", "2", "3", "4"}:
            print("\nChoose an option from 1 to 5.")
            continue

        try:
            if choice == "4":
                entered = input("\nEnter items separated by commas: ")
                items = [item.strip() for item in entered.split(",") if item.strip()]
                target = input("Enter the item to find: ").strip()
                print(f"\nFound: {search(items, target)}")
                continue

            n = int(input("\nEnter a nonnegative whole number: "))
            if n < 0:
                print("\nEnter 0 or a positive whole number.")
                continue

            if choice == "1":
                print(f"\nFactorial of {n}: {factorial(n)}")
            elif choice == "2":
                print(f"\nFibonacci F({n}): {fibonacci(n)}")
                first_terms = [fibonacci(index) for index in range(n)]
                print(f"First {n} Fibonacci terms: {first_terms}")
            else:
                print(f"\nSum from 1 to {n}: {sum_numbers(n)}")

        except ValueError:
            print("\nEnter 0 or a positive whole number.")
        except RecursionError:
            print("\nTry a smaller number or a shorter list.")


if __name__ == "__main__":
    main()