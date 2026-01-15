import sys
import os
import json
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from game.movie_repository import MovieRepository


class TestMovieRepository(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_movies.json"
        with open(self.test_file, "w") as f:
            json.dump({"movies": ["Inception", "Titanic"]}, f)

        self.repo = MovieRepository(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_movies(self):
        movies = self.repo.read_movies()
        self.assertEqual(movies, ["Inception", "Titanic"])

   