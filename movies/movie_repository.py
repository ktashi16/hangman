from pathlib import Path
import json


class MovieRepository:
    def __init__(self, filename="movies.json"):
        self.filepath = Path(filename)
        self._ensure_file_exists()

    #check file exists
    def _ensure_file_exists(self):
        if not self.filepath.exists():
            with open(self.filepath, "w") as file:
                json.dump({"movies": []}, file)
            
    def read_movies(self):
        with open(self.filepath, "r") as file:
            data = json.load(file)
            return data["movies"]
    
    def create_movie(self, title):
        title = title.strip()
        if not title:
            raise ValueError("Movie title cannot be empty")

        movies = self.read_movies()

        if title in movies:
            raise ValueError("Movie already exists")

        movies.append(title)

        with open(self.filepath, "w") as file:
            json.dump({"movies": movies}, file, indent=4)



if __name__ == "__main__":
    repo = MovieRepository()
    repo.create_movie("") #testing
    repo.create_movie("Inception")
    print(repo.read_movies())

