import random


class HangmanGame:
    def __init__(self, movies):
        self.word = random.choice(movies).upper()  #selecting a random word from movies.json
        self.masked_word = self._mask_word()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.won = False
        self.lost = False

     
    def _mask_word(self):
        masked = ""
        for char in self.word:
            if char == " ":
                masked += " "
            else:
                masked += "_"
        return masked

    def guess_letter(self, letter):
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Guess must be a single letter")

        letter = letter.upper()


if __name__ == "__main__":
    movies = ["Inception", "Interstellar"]
    game = HangmanGame(movies)
    game.guess_letter("AB")


