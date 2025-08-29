import sys
sys.path.insert(0, 'src')
from src.config.settings import SessionLocal, engine
from src.models.guess import Guess
from sqlalchemy.orm import Session

# Test if guesses are being saved to the database
def test_guesses():
    db = SessionLocal()
    try:
        # Get all guesses from the database
        guesses = db.query(Guess).all()
        print(f"Total guesses in database: {len(guesses)}")
        
        if guesses:
            print("Guesses found:")
            for guess in guesses:
                print(f"ID: {guess.id}, Game ID: {guess.game_id}, Word: {guess.guess_word}, Position: {guess.position}, Feedback: {guess.feedback}")
        else:
            print("No guesses found in the database")
            
    except Exception as e:
        print(f"Error querying guesses: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_guesses()
