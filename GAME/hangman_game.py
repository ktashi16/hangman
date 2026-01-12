import random


class HangmanGame:
    def __init__(self, movies):
        self.word = random.choice(movies).upper()  #selecting a random word from movies.json
        self.masked_word = self._mask_word()
        
    def _mask_word(self):
        masked = ""
        for char in self.word:
            if char == " ":
                masked += " "
            else:
                masked += "_"
        return masked



if __name__ == "__main__":
    movies = ["Inception", "Interstellar"]
    game = HangmanGame(movies)
    print("Chosen word:", game.word)
    print("Masked:", game.masked_word)
