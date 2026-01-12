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
        MAX_GUESSES = 7
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Guess must be a single letter")
        
        if letter in self.guessed_letters:
            raise ValueError("Letter already guessed")

        letter = letter.upper()

        if letter in self.word:
            self._reveal_letter(letter)
        else:
            self.incorrect_guesses += 1

        if self.incorrect_guesses >= MAX_GUESSES:
            self.lost = True
            self.masked_word = self.word

        if self.masked_word == self.word:
            self.won = True

    def guess_word(self, word):
        if word.upper() == self.word:
            self.masked_word = self.word
            self.won = True
        else:
            self.incorrect_guesses += 1

    def _reveal_letter(self, letter):
        masked = list(self.masked_word)
        for i, char in enumerate(self.word):
            if char == letter:
                masked[i] = letter
        self.masked_word = "".join(masked)


if __name__ == "__main__":
    movies = ["Inception", "Interstellar"]
    game = HangmanGame(movies)
    game.guess_word("Inception")




