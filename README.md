# Wordle CLI Python

A command-line interface (CLI) implementation of the popular Wordle game built in Python. This project uses SQLAlchemy ORM with a PostgreSQL database backend to manage users, games, guesses, and word lists. The game features user login, game statistics, and a rich terminal UI powered by the Rich library.

## Features

- User login and authentication (basic)
- Play Wordle game in the terminal with a 5-letter word guessing challenge
- Persistent game state stored in PostgreSQL database
- Track game statistics and user progress
- Seed database with a curated list of valid 5-letter words
- Rich terminal UI with colors and styled text using Rich library
- Database migrations managed with Alembic

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd phase3-wordle-clone/wordle-cli-python
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, install using `setup.py`:

   ```bash
   pip install .
   ```

4. Set up environment variables for PostgreSQL connection (optional, defaults are set in code):

   ```bash
   export DB_USERNAME=your_db_username
   export DB_PASSWORD=your_db_password
   export DB_HOST=your_db_host
   export DB_PORT=5432
   export DB_NAME=your_db_name
   ```

5. Run database migrations to create tables:

   ```bash
   alembic upgrade head
   ```

6. Seed the database with words:

   ```bash
   python -m src.data.seed_data
   ```

## Usage

Run the Wordle CLI game:

```bash
wordle
```

Or run directly with Python:

```bash
python -m src.main
```

Follow the on-screen prompts to log in, start a new game, view statistics, or exit.

## Project Structure

- `src/`
  - `models/` - SQLAlchemy ORM models for User, Game, Guess, Word
  - `services/` - Business logic for game flow, word selection, stats, authentication
  - `views/` - Terminal UI views for login, menu, game play, statistics
  - `data/` - Seed data and word list JSON
  - `config/` - Configuration and database settings
  - `utils/` - Helper functions and CLI styling utilities
  - `main.py` - Application entry point

- `migrations/` - Alembic database migration scripts
- `setup.py` - Project setup and dependencies
- `README.md` - Project documentation

## Technologies Used

- Python 3
- SQLAlchemy ORM
- PostgreSQL (Supabase)
- Alembic for migrations
- Rich library for terminal UI
- bcrypt for password hashing (planned/partial)

## Database

The project uses PostgreSQL to store:

- Users and their credentials
- Games and their status (in progress, won, lost)
- Guesses made in each game with feedback
- Valid 5-letter words for the game

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Authors
Fidel Martins Otieno
Benson Beckham
Jaylan Saad
Abdiaziz Ali
Joy Hassan

## License

This project is licensed under the MIT License.
