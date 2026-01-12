from movie_repository import MovieRepository


def print_admin_menu():
    print("\n🎬 Movie Admin Menu")
    print("1. Add movie")
    print("2. View movies")
    print("3. Update movie")
    print("4. Delete movie")
    print("5. Exit")


def handle_admin_choice(choice, repo):
    if choice == "1":
        repo.create_movie(input("Movie title: "))
        print("Movie added")

    elif choice == "2":
        for movie in repo.read_movies():
            print("-", movie)

    elif choice == "3":
        repo.update_movie(
            input("Old title: "),
            input("New title: ")
        )
        print("Movie updated")

    elif choice == "4":
        repo.delete_movie(input("Movie title: "))
        print("Movie deleted")

    elif choice == "5":
        return False

    else:
        print("Invalid option")

    return True


def movie_admin_menu():
    repo = MovieRepository()
    running = True

    while running:
        print_admin_menu()
        choice = input("Choose: ")

        try:
            running = handle_admin_choice(choice, repo)
        except ValueError as e:
            print("Error", e)


if __name__ == "__main__":
    movie_admin_menu()
