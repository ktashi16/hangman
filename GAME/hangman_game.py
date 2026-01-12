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
        self.max_guesses = max_guesses  # added for consistency

        
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
        if letter in self.guessed_letters:
            raise ValueError("Letter already guessed")

        self.guessed_letters.add(letter)

        if letter in self.word:
            self._reveal_letter(letter)
        else:
            self.incorrect_guesses += 1

        if self.incorrect_guesses >= self.max_guesses:
            self.lost = True
            self.reveal_word()

        if self.masked_word == self.word:
            self.won = True


    def guess_word(self, guessed_word):
        guessed_word = guessed_word.upper()
        if self.is_over():  # ignore input if game is over
            return

        if guessed_word == self.word:
            self.won = True
            self.reveal_word()  # show full word
        else:
            self.incorrect_guesses += 1
            if self.incorrect_guesses >= self.max_guesses:
                self.lost = True
                self.reveal_word()  # show full word if losing

    def is_over(self):
        return self.won or self.lost



    def reveal_word(self):
        self.masked_word = self.word




    def _reveal_letter(self, letter):
        masked = list(self.masked_word)
        for i, char in enumerate(self.word):
            if char == letter:
                masked[i] = letter
        self.masked_word = "".join(masked)

    def remaining_letters(self):
        return set(string.ascii_uppercase) - self.guessed_letters


if __name__ == "__main__":
    movies = ["Inception", "Interstellar"]
    game = HangmanGame(movies)
    game.guess_word("Inception")




