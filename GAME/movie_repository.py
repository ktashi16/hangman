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
        try:
            with open(self.filepath, "r") as file:
                return json.load(file)["movies"]
        except json.JSONDecodeError:
            raise ValueError("Movie file is corrupted")

    
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


    def update_movie(self, old_title, new_title):
            
        movies = self.read_movies()

        if old_title not in movies:
            raise ValueError("Movie not found")

        index = movies.index(old_title)
        movies[index] = new_title.strip()

        with open(self.filepath, "w") as file:
            json.dump({"movies": movies}, file, indent=4)


    def delete_movie(self, title):
        movies = self.read_movies()

        if title not in movies:
            raise ValueError("Movie not found")

        movies.remove(title)

        with open(self.filepath, "w") as file:
            json.dump({"movies": movies}, file, indent=4)

if __name__ == "__main__":
    repo = MovieRepository()


