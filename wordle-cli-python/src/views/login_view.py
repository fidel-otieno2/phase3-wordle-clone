from rich.console import Console
from sqlalchemy.orm import Session
from src.services.auth_service import get_or_create_test_user
from src.services.game_service import get_user_current_game

console = Console()

def login_user(db: Session):
    """Handle user login and check for ongoing games"""
    console.print("[bold green]Welcome to the Wordle Game![/bold green]")
    
    username = console.input("Enter your username: ")
    password = console.input("Enter your password: ")
    
    # Here you would typically validate the username and password
    # For now, we will just create or get the test user
    user = get_or_create_test_user(db)
    
    console.print(f"[bold blue]Logged in as: {user.username}[/bold blue]")
    
    # Check if user has an ongoing game
    ongoing_game = get_user_current_game(db, user.id)
    
    return user.id, ongoing_game