import random


class HangmanGame:
    def __init__(self, movies):
        self.word = random.choice(movies) #selecting a random word from movies.json


if __name__ == "__main__":
    movies = ["Inception", "Interstellar"]
    game = HangmanGame(movies)
    print("Chosen word:", game.word)
