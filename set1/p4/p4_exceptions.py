
# P4: Safe Menu Program
# Topics: Exception Handling

def show_menu():
    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Divide Two Numbers")
    print("2. Open a File")
    print("3. Exit")
    print("=============================")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("Division feature coming soon.")

        elif choice == "2":
            print("File opening feature coming soon.")

        elif choice == "3":
            print("Thank you!!!")
            break

        else:
            print("Invalid menu choice. Please try again.")


if __name__ == "__main__":
    main()
