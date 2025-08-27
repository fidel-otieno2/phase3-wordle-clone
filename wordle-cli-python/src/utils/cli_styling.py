from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.text import Text
from rich.style import Style

# Custom theme for the Wordle game
custom_theme = Theme({
    "success": "bold green",
    "error": "bold red",
    "warning": "bold yellow",
    "info": "bold blue",
    "highlight": "bold magenta",
    "correct": "bold white on green",
    "present": "bold white on yellow",
    "absent": "bold white on red",
    "background": "on blue",
    "title": "bold white on blue",
})

console = Console(theme=custom_theme)

def print_welcome():
    """Print a welcome message with styling"""
    console.print(Panel.fit(
        "[title]🎯 Welcome to Wordle CLI Game![/title]",
        subtitle="Guess the 5-letter word",
        style="background"
    ))

def print_game_status(status_message, style="info"):
    """Print game status messages with styling"""
    console.print(f"[{style}]{status_message}[/{style}]")

def print_guess_feedback(guess, feedback):
    """Print guess feedback with color coding"""
    colored_guess = Text()
    for i, letter in enumerate(guess.upper()):
        if feedback[i] == 'correct':
            colored_guess.append(letter, style="correct")
        elif feedback[i] == 'present':
            colored_guess.append(letter, style="present")
        else:
            colored_guess.append(letter, style="absent")
        colored_guess.append(" ")
    
    console.print(colored_guess)

def print_game_over(word, won=False):
    """Print game over message"""
    if won:
        message = f"🎉 Congratulations! You guessed the word: [highlight]{word}[/highlight]"
        style = "success"
    else:
        message = f"😢 Game Over! The word was: [highlight]{word}[/highlight]"
        style = "error"
    
    console.print(Panel.fit(
        message,
        style=style
    ))