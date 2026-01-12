from admin import movie_admin_menu


def print_main_menu():
    print("\n🎮 Main Menu")
    print("1. Play Hangman")
    print("2. Admin Menu")
    print("3. Exit")


def main():
    running = True

    while running:
        print_main_menu()
        choice = input("Choose: ")

        if choice == "1":
            print("GAME")

        elif choice == "2":
            movie_admin_menu()

        elif choice == "3":
            running = False

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
