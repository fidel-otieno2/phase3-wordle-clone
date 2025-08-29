# Wordle CLI Python

A comprehensive command-line interface (CLI) implementation of the popular Wordle game built in Python. This project uses SQLAlchemy ORM with a PostgreSQL database backend to manage users, games, guesses, and word lists. The game features user authentication, game statistics tracking, and a rich terminal UI powered by the Rich library.

## 🎯 Features

### Core Gameplay
- **Word Guessing Challenge**: Guess 5-letter words with 6 attempts per game
- **Real-time Feedback**: Color-coded feedback for each guess (green for correct position, yellow for correct letter wrong position, gray for incorrect letters)
- **Game State Persistence**: Save and resume games across sessions
- **Daily Word Challenge**: New word available each day for all players

### User Management
- **User Registration & Login**: Secure user authentication system
- **Password Security**: bcrypt password hashing for secure credential storage
- **User Profiles**: Track individual user statistics and game history
- **Session Management**: Persistent login sessions

### Statistics & Analytics
- **Win/Loss Tracking**: Monitor game performance over time
- **Guess Distribution**: Analyze guess patterns and success rates
- **Streak Tracking**: Track consecutive wins and longest streaks
- **Performance Metrics**: Calculate average guesses and success percentage

### Technical Features
- **Database Integration**: PostgreSQL with SQLAlchemy ORM
- **Database Migrations**: Alembic for schema versioning and updates
- **Rich Terminal UI**: Beautiful CLI interface with colors and styling
- **Input Validation**: Comprehensive validation for words and user inputs
- **Error Handling**: Robust error handling and user-friendly error messages

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database (local or cloud-based like Supabase)
- pip package manager

### Step-by-Step Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd phase3-wordle-clone/wordle-cli-python
   ```

2. **Create and activate a Python virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or install using setup.py:
   ```bash
   pip install .
   ```

4. **Database Configuration**:
   Set up environment variables for PostgreSQL connection:
   ```bash
   export DB_USERNAME=your_db_username
   export DB_PASSWORD=your_db_password
   export DB_HOST=your_db_host
   export DB_PORT=5432
   export DB_NAME=your_db_name
   ```

   Default values (for development):
   - DB_USERNAME: postgres
   - DB_PASSWORD: password
   - DB_HOST: localhost
   - DB_PORT: 5432
   - DB_NAME: wordle_db

5. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

6. **Seed the database with words**:
   ```bash
   python -m src.data.seed_data
   ```

## 🎮 Usage

### Starting the Game
Run the Wordle CLI game:
```bash
wordle
```
Or run directly with Python:
```bash
python -m src.main
```

### Game Flow
1. **Login/Register**: Enter your username and password
2. **Main Menu**: Choose from:
   - Start New Game
   - View Statistics
   - Continue Previous Game (if available)
   - Logout
   - Exit

3. **Gameplay**:
   - Enter 5-letter words as guesses
   - Receive color-coded feedback after each guess
   - Game ends when you guess correctly or use all 6 attempts

### Example Game Session
```
Welcome to Wordle CLI!
Username: player1
Password: ******

Main Menu:
1. Start New Game
2. View Statistics
3. Continue Game
4. Logout
5. Exit

Choose option: 1

Attempt 1/6: crane
🟨 🟨 ⬜ ⬜ 🟩

Attempt 2/6: plate
⬜ 🟩 🟩 🟩 🟩

Attempt 3/6: slate
🟩 🟩 🟩 🟩 🟩

Congratulations! You guessed the word in 3 attempts!
```

## ⚙️ Configuration

### Environment Variables
The application supports the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `DB_USERNAME` | PostgreSQL username | `postgres` |
| `DB_PASSWORD` | PostgreSQL password | `password` |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |
| `DB_NAME` | Database name | `wordle_db` |
| `DEBUG` | Enable debug mode | `False` |

### Database Setup
The application uses PostgreSQL with the following schema:

#### Tables
- **users**: User accounts and authentication
- **games**: Game sessions and outcomes
- **guesses**: Individual guesses with feedback
- **words**: Valid 5-letter words for the game

## 🏗️ Project Structure

```
wordle-cli-python/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── models/                 # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── user.py            # User model with authentication
│   │   ├── game.py            # Game session model
│   │   ├── guess.py           # Guess model with feedback
│   │   └── word.py            # Word dictionary model
│   ├── services/              # Business logic layer
│   │   ├── __init__.py
│   │   ├── auth_service.py    # Authentication logic
│   │   ├── game_service.py    # Game flow management
│   │   ├── stats_service.py   # Statistics calculation
│   │   └── word_service.py    # Word selection and validation
│   ├── views/                 # Terminal UI components
│   │   ├── __init__.py
│   │   ├── game_view.py       # Gameplay interface
│   │   ├── login_view.py      # Login/registration interface
│   │   ├── menu_view.py       # Main menu interface
│   │   └── stats_view.py      # Statistics display
│   ├── data/                  # Data management
│   │   ├── __init__.py
│   │   ├── seed_data.py       # Database seeding
│   │   └── words.json         # Word list
│   ├── config/                # Configuration
│   │   ├── __init__.py
│   │   ├── constants.py       # Application constants
│   │   └── settings.py        # Database and app settings
│   └── utils/                 # Utility functions
│       ├── __init__.py
│       ├── cli_styling.py     # Rich terminal styling
│       ├── helpers.py         # Helper functions
│       └── validators.py      # Input validation
├── migrations/                # Database migrations
│   ├── env.py
│   ├── script.py.mako
│   └── versions/              # Migration scripts
├── setup.py                   # Package configuration
├── requirements.txt           # Dependencies
├── alembic.ini               # Alembic configuration
└── .gitignore
```

## 🔧 Development

### Running the Application
```bash
# Development mode with debug output
python -m src.main --debug

# Or install and run as package
pip install -e .
wordle --debug
```

### Database Operations
```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Downgrade migrations
alembic downgrade -1

# Seed database with words
python -m src.data.seed_data
```

### Code Organization
- **Models**: Define database schema and relationships
- **Services**: Contain business logic and data operations
- **Views**: Handle terminal UI and user interaction
- **Utils**: Provide reusable helper functions
- **Config**: Manage application settings and constants

## 🗄️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    current_game_id INTEGER REFERENCES games(id)
);
```

### Games Table
```sql
CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    target_word VARCHAR(5) NOT NULL,
    status VARCHAR(20) DEFAULT 'in_progress',
    attempts INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);
```

### Guesses Table
```sql
CREATE TABLE guesses (
    id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games(id),
    guess_word VARCHAR(5) NOT NULL,
    feedback VARCHAR(5) NOT NULL,
    attempt_number INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Words Table
```sql
CREATE TABLE words (
    id SERIAL PRIMARY KEY,
    word VARCHAR(5) UNIQUE NOT NULL,
    is_valid BOOLEAN DEFAULT TRUE
);
```

## 🔐 Authentication

### Password Security
- Uses bcrypt for secure password hashing
- Salt rounds configured for optimal security
- Passwords are never stored in plain text

### Session Management
- User sessions persist across game sessions
- Automatic logout after extended inactivity
- Secure credential handling

## 🎨 User Interface

### Rich Library Integration
- Color-coded feedback using emoji and colored text
- Formatted tables for statistics display
- Progress bars and status indicators
- Consistent styling throughout the application

### Input Validation
- 5-letter word validation
- Dictionary word checking
- Case-insensitive input handling
- Error messages with helpful suggestions

## 🐛 Troubleshooting

### Common Issues

**Database Connection Errors**
```bash
# Check if PostgreSQL is running
sudo service postgresql status

# Verify connection settings
echo $DB_USERNAME $DB_HOST $DB_PORT
```

**Migration Issues**
```bash
# Reset and recreate database
alembic downgrade base
alembic upgrade head
```

**Package Installation Issues**
```bash
# Clear cache and reinstall
pip cache purge
pip install --force-reinstall -r requirements.txt
```

### Debug Mode
Enable debug mode for detailed error messages:
```bash
python -m src.main --debug
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests if applicable
4. Commit your changes: `git commit -m 'Add amazing feature'`
5. Push to the branch: `git push origin feature/amazing-feature`
6. Open a pull request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write meaningful commit messages
- Add comments for complex logic
- Update documentation for new features
- Test changes thoroughly

## 📊 API Reference (Internal)

### Game Service Methods
- `start_new_game(user_id)`: Starts a new game session
- `make_guess(game_id, guess_word)`: Processes a guess and returns feedback
- `get_game_status(game_id)`: Returns current game state
- `end_game(game_id, status)`: Finalizes game outcome

### Auth Service Methods
- `register_user(username, password)`: Creates new user account
- `authenticate_user(username, password)`: Validates user credentials
- `get_user_stats(user_id)`: Retrieves user statistics

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Fidel Martins Otieno
- Benson Beckham  
- Jaylan Saad
- Abdiaziz Ali
- Joy Hassan

## 🙏 Acknowledgments

- Inspired by the original Wordle game by Josh Wardle
- Built with Python, SQLAlchemy, PostgreSQL, and Rich library
- Thanks to the open-source community for valuable tools and libraries

---

**Happy Wordling!** 🎯✨
