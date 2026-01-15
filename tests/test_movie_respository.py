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

    def test_create_movie(self):
        self.repo.create_movie("Interstellar")
        self.assertIn("Interstellar", self.repo.read_movies())

    def test_create_duplicate_movie_raises_error(self):
        with self.assertRaises(ValueError):
            self.repo.create_movie("Inception")

    def test_delete_movie(self):
        self.repo.delete_movie("Titanic")
        self.assertNotIn("Titanic", self.repo.read_movies())

    def test_update_movie(self):
        self.repo.update_movie("Inception", "Inception (2010)")
        movies = self.repo.read_movies()
        self.assertIn("Inception (2010)", movies)
        self.assertNotIn("Inception", movies)



if __name__ == "__main__":
    unittest.main()
