from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from ..utils.cli_styling import get_theme

console = Console()
theme = get_theme()

def show_main_menu():
    """Display the main menu"""
    console.clear()
    console.print(
        Panel.fit(
            "[bold]🎯 WORDLE CLI GAME[/bold]",
            style=theme["primary"],
            subtitle="Welcome to the Wordle Challenge!"
        )
    )
    
    console.print("\n[bold]Main Menu:[/bold]")
    console.print("1. 🎮 Start New Game")
    console.print("2. 📊 View Statistics")
    console.print("3. ℹ️  Game Instructions")
    console.print("4. 🚪 Exit")
    
    choice = Prompt.ask(
        "\nSelect an option (1-4)",
        choices=["1", "2", "3", "4"],
        default="1"
    )
    
    return choice

def show_game_menu():
    """Display the in-game menu"""
    console.print("\n[bold]Game Menu:[/bold]")
    console.print("1. 🔄 Make a Guess")
    console.print("2. 🏃‍♂️ Give Up")
    console.print("3. ↩️  Return to Main Menu")
    
    choice = Prompt.ask(
        "Select an option (1-3)",
        choices=["1", "2", "3"],
        default="1"
    )
    
    return choice

def show_instructions():
    """Display game instructions"""
    console.clear()
    console.print(
        Panel.fit(
            "[bold]📖 GAME INSTRUCTIONS[/bold]",
            style=theme["secondary"],
            subtitle="How to Play Wordle"
        )
    )
    
    instructions = """
    🎯 Objective: Guess the 5-letter word in 6 attempts or less.
    
    🟩 Green: Letter is correct and in the right position.
    🟨 Yellow: Letter is in the word but in the wrong position.
    ⬜ Gray: Letter is not in the word.
    
    💡 Tips:
    - Start with common vowels and consonants
    - Use process of elimination
    - Pay attention to letter positions
    
    Press Enter to return to the main menu...
    """
    
    console.print(instructions)
    input()

def show_statistics(stats: dict):
    """Display user statistics"""
    console.clear()
    console.print(
        Panel.fit(
            "[bold]📊 YOUR STATISTICS[/bold]",
            style=theme["info"],
            subtitle="Game Performance Overview"
        )
    )
    
    if stats['total_games'] == 0:
        console.print("No games played yet. Start playing to see your stats!")
    else:
        console.print(f"🎮 Total Games: {stats['total_games']}")
        console.print(f"✅ Games Won: {stats['games_won']}")
        console.print(f"❌ Games Lost: {stats['games_lost']}")
        console.print(f"📈 Win Percentage: {stats['win_percentage']:.1f}%")
    
    console.print("\nPress Enter to continue...")
    input()