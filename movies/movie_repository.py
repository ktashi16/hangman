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
    

if __name__ == "__main__":
    repo = MovieRepository()
    print("File path:", repo.filepath)
