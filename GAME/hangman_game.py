import random
import string

class HangmanGame:
    def __init__(self, movies, max_guesses=7):
        self.word = random.choice(movies).upper()
        self.masked_word = self._mask_word()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.won = False
        self.lost = False
        self.max_guesses = max_guesses

    def _mask_word(self):
        return "".join("_" if c != " " else " " for c in self.word)

    def guess_letter(self, letter):
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Guess must be a single letter")

        letter = letter.upper()
        if letter in self.guessed_letters:
            raise ValueError("Letter already guessed")

        self.guessed_letters.add(letter)

        if letter in self.word:
            self._reveal_letter(letter)
        else:
            self.incorrect_guesses += 1

        # Check for losing first
        if self.incorrect_guesses >= self.max_guesses:
            self.lost = True
            self.reveal_word()
        # Then check for winning only if not lost
        elif self.masked_word == self.word:
            self.won = True

    def guess_word(self, guessed_word):
        guessed_word = guessed_word.upper()
        if self.is_over():
            return

        if guessed_word == self.word:
            self.won = True
            self.reveal_word()
        else:
            self.incorrect_guesses += 1
            if self.incorrect_guesses >= self.max_guesses:
                self.lost = True
                self.reveal_word()

    def _reveal_letter(self, letter):
        masked = list(self.masked_word)
        for i, c in enumerate(self.word):
            if c == letter:
                masked[i] = letter
        self.masked_word = "".join(masked)

    def reveal_word(self):
        self.masked_word = self.word

    def is_over(self):
        return self.won or self.lost

    def remaining_letters(self):
        return set(string.ascii_uppercase) - self.guessed_letters


if __name__ == "__main__":
    movies = ["Inception", "Interstellar", "Finding Nemo"]
    game = HangmanGame(movies)

    while not game.is_over():
        print(f"\nWord: {game.masked_word}")
        print(f"Guessed letters: {', '.join(sorted(game.guessed_letters))}")
        print(f"Remaining letters: {', '.join(sorted(game.remaining_letters()))}")
        print(f"Incorrect guesses: {game.incorrect_guesses}/{game.max_guesses}")

        guess = input("Guess a letter or full movie title: ").strip()
        if len(guess) == 1:
            try:
                game.guess_letter(guess)
            except ValueError as e:
                print(f"Error {e}")
        else:
            game.guess_word(guess)

    if game.won:
        print(f"\n You guessed it! The movie was: {game.masked_word}")
    else:
        print(f"\n You lost! The movie was: {game.masked_word}")
