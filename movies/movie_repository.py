from pathlib import Path
import json


class MovieRepository:
    def __init__(self, filename="movies.json"):
        self.filepath = Path(filename)

if __name__ == "__main__":
    repo = MovieRepository()
    print("File path:", repo.filepath)
