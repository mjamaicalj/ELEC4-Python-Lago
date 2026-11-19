# Name: Ma. Jamaica LJ J. Lago
# Section: IV-BSIT A
# Activity: P4 - Safe Menu Program
# Date: November 19, 2026


def show_menu():
    print("\n===== SAFE MENU PROGRAM =====")
    print("Student: Ma. Jamaica LJ J. Lago")
    print("1. Divide Two Numbers")
    print("2. Open a File")
    print("3. Exit")
    print("=============================")


# Function to divide two numbers safely
def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2

    except ValueError:
        print("Error: Please enter valid numbers only.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print(f"Result: {result}")

    finally:
        print("Division attempt finished.")


# Function to open and read a file safely
def open_file():
    filename = input("Enter file name: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: The specified file was not found.")

    except (OSError, ValueError):
        print("Error: Unable to read the specified file.")

    else:
        print("\n===== FILE CONTENT =====")
        print(content)
        print("========================")

    finally:
        print("File read attempt finished.")


# Main function for the menu-driven program
def main():
    while True:
        show_menu()

        try:
            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                divide_numbers()

            elif choice == "2":
                open_file()

            elif choice == "3":
                print("Thank you for using the program!")
                break

            else:
                print("Invalid menu choice. Please choose 1, 2, or 3.")

        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Exiting safely.")
            break


if __name__ == "__main__":
    main()