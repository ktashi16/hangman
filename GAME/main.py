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
        choice = input("Choose: ")

        if choice == "1":
            print("GAME")

        elif choice == "2":
            movie_admin_menu()

        elif choice == "3":
            running = False

        else:
            print("Invalid choice")


def play_game():
    repo = MovieRepository("movies.json")
    game = HangmanGame(repo.get_all_movies())

    while not game.is_over():
        print(f"\nWord: {game.masked_word}")
        print(f"Guessed letters: {', '.join(sorted(game.guessed_letters))}")
        print(f"Incorrect guesses: {game.incorrect_guesses}/{game.max_guesses}")

        choice = input("Guess a letter or the full movie title: ").strip()
        if len(choice) == 1:
            try:
                game.guess_letter(choice)
            except ValueError as e:
                print(f"Error {e}")
        elif len(choice) > 1:
            game.guess_word(choice)
        else:
            print("Invalid input. Please guess a letter or a word.")

    if game.won:
        print(f"You guessed it! The movie was: {game.masked_word}")
    else:
        print(f"You lost! The movie was: {game.masked_word}")




if __name__ == "__main__":
    main()
