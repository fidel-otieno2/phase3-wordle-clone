import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rich.console import Console
from src.config.settings import Base, SQLALCHEMY_DATABASE_URL, SessionLocal
from src.views.game_view import play_game
from src.views.login_view import login_user
from src.services.game_service import start_new_game
from src.services.word_service import get_random_word
from src.data.seed_data import seed_words

console = Console()

def main():
    # Set up the database
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(engine)
    
    # Seed the database with words
    seed_words()
    
    # Start a session
    db = SessionLocal()
    
    # User login
    user_id, ongoing_game = login_user(db)
    
    if ongoing_game:
        console.print("[bold green]Resuming your previous game...[/bold green]")
        play_game(db, ongoing_game.id)
    else:
        console.print("[bold green]Starting a new Wordle Game...[/bold green]")
        target_word_obj = get_random_word(db)
        new_game = start_new_game(db, user_id, target_word_obj.word)
        play_game(db, new_game.id)

if _name_ == "_main_":
    main()