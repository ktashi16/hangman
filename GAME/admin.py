from movie_repository import MovieRepository

def print_admin_menu():
    print("\n Admin Menu")
    print("1. Add Movie")
    print("2. Update Movie")
    print("3. Delete Movie")
    print("4. View All Movies")
    print("5. Back to Main Menu")


def handle_admin_choice(choice, repo):
    if choice == "1":
        movie_name = input("Enter movie name to add: ").strip()
        try:
            repo.create_movie(movie_name)
            print(f"Success '{movie_name}' added successfully.")
        except ValueError as e:
            print(f"Error {e}")

    elif choice == "2":
        old_name = input("Enter the movie name to update: ").strip()
        new_name = input("Enter the new name: ").strip()
        try:
            repo.update_movie(old_name, new_name)
            print(f"Success '{old_name}' updated to '{new_name}'.")
        except ValueError as e:
            print(f"Error {e}")

    elif choice == "3":
        movie_name = input("Enter movie name to delete: ").strip()
        try:
            repo.delete_movie(movie_name)
            print(f"Success '{movie_name}' deleted successfully.")
        except ValueError as e:
            print(f"Error {e}")

    elif choice == "4":
        movies = repo.read_movies()
        if movies:
            print("\nMovies:")
            for m in movies:
                print(f"- {m}")
        else:
            print("No movies available.")

    elif choice == "5":
        return False  # exit admin menu

    else:
        print("Invalid choice")
    
    return True  # stay in admin menu


def movie_admin_menu():
    repo = MovieRepository()
    running = True

    while running:
        print_admin_menu()
        choice = input("Choose: ")
        running = handle_admin_choice(choice, repo)
