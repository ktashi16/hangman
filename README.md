# Guess the Movie Game

## Overview

This project is a **CLI-based Hangman game** built in Python, integrated with a simple **CRUD backend** for storing movie titles. The project demonstrates **object-oriented programming, modular design, file-based persistence, and unit testing**.

Players can guess letters or full movie titles stored in a JSON file, while an admin menu allows viewing, adding, updating, or deleting movies. This structure keeps game logic separate from data management and CLI, making the system **maintainable, scalable, and testable**.

---

## Features

* **Play Hangman**

  * Guess single letters or full movie titles.
  * Tracks guessed letters and incorrect guesses.
  * Handles edge cases with incorrect input such as invalid characters, repeated letter guesses and also case-insensitive comparisons.

* **Admin Menu**

  * Add, update, read, or delete movies from the repository.
  * Validates inputs to prevent duplicates or empty titles.

* **Modular Design**

  * `hangman_game.py` – contains the core Hangman logic.
  * `movie_repository.py` – handles CRUD operations on movies stored in `movies.json`.
  * `admin.py` – CLI interface for administrative tasks.
  * `main.py` – Entry point with option to play game or administrative task

* **Persistence**

  * Uses a JSON file (`movies.json`) for storing movie titles.
  * Designed to allow switching to a database with minimal changes.

* **Testing**

  * Unit tests written using Python’s `unittest` framework.
  * Tests cover CRUD operations 

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ktashi16/hangman.git
cd hangman/game
```

2. Make sure Python 3.x is installed:

```bash
python --version
```

3. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

---

## Usage

Run the project from the game dir.

```bash
python main.py
```

### Main Menu Options

1. **Play Hangman** – Hangman game to guess movie titles
2. **Admin Menu** – Add, Update, Delete and View Movies
3. **Exit** – quit the application.

---


## Admin Menu Commands

* **Add Movie** – create a new movie title.
* **List Movies** – read all stored movies.
* **Update Movie** – update an existing movie.
* **Delete Movie** – delete a movie.
* **Exit Admin Menu** – return to main menu.

---

## Project Structure

```
hangman/
│── game/
│   ├── hangman_game.py       # Hangman game logic
│   ├── movie_repository.py   # CRUD backend for movies
│   ├── admin.py              # CLI for admin tasks
│   ├── main.py               # Entry point for the program
│   ├── movies.json           # Stores movie titles
├── tests/                # Unit tests
│   └── test_movie_repository.py
├── README.md
```

---

## Unit Tests

Unit tests are written using Python’s `unittest` framework.

---

## Future Improvements

- **Admin authentication** – only users with admin privileges can access the admin menu.  
- **User accounts** – allow users to log in and save scores and game history.  
- **Scalability & reliability** – make the game and backend robust for many users and larger datasets.  
- **Security system** – implement proper validation, authentication, and protection against malicious inputs.  
- **Enhanced persistence** – move from JSON files to a database for more reliable storage.  
- **Scoring and leaderboards** – track progress and stats for players.


