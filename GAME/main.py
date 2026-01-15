from hangman_game import HangmanGame
from movie_repository import MovieRepository
from admin import movie_admin_menu

def print_main_menu():
    print("\n Main Menu")
    print("1. Play Hangman")
    print("2. Admin Menu")
    print("3. Exit")


def main():
    running = True

    while running:
        print_main_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            play_game()  

        elif choice == "2":
            movie_admin_menu()

        elif choice == "3":
            running = False

        else:
            print("Invalid choice")


def play_game():
    repo = MovieRepository("movies.json")
    movies = repo.read_movies()

    if not movies:
        print("No movies available to play. Add some from the admin menu first.")
        return

    game = HangmanGame(movies)

    while not game.is_over():
        print(f"\nWord: {game.masked_word}")
        print(f"Guessed letters: {', '.join(sorted(game.guessed_letters))}")
        print(f"Incorrect guesses: {game.incorrect_guesses}/{game.max_guesses}")

        choice = input("Guess a letter or the full movie title: ").strip()
        try:
            if len(choice) == 1:
                game.guess_letter(choice)
            elif len(choice) > 1:
                game.guess_word(choice)
            else:
                print("Invalid input. Please enter a letter or movie title.")
        except (ValueError, TypeError) as e:
            print(f"Error {e}")
    if game.won:
        print(f"You guessed it! The movie was: {game.masked_word}")
    else:
        print(f"You lost! The movie was: {game.masked_word}")


if __name__ == "__main__":
    main()
