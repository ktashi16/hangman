from movie_repository import MovieRepository


def movie_admin_menu():
    while True:
        print("\n🎬 Movie Admin Menu")
        print("1. Add movie")
        print("2. View movies")
        print("3. Update movie")
        print("4. Delete movie")
        print("5. Exit")

        repo = MovieRepository()

        choice = input("Choose an option: ")


        if choice == "1":
            title = input("Movie title: ")
            repo.create_movie(title)
            print(f"Movie added: {title}")

        elif choice == "2":
            movies = repo.read_movies()
            print("\nMovies:")
            for movie in movies:
                print("-", movie)

        elif choice == "3":
            print("Updating")
        
        elif choice == "4":
            print("Deleting")
                
        elif choice == "5":
            break


if __name__ == "__main__":
    repo = MovieRepository()
    print("Admin file connected to repository")
