import sys
sys.path.insert(0, 'src')
from src.config.settings import SessionLocal, engine
from src.models.user import User
from src.models.game import Game
from src.services.game_service import set_user_current_game, get_user_current_game, clear_user_current_game, start_new_game
from src.services.word_service import get_random_word
from sqlalchemy.orm import Session

def test_current_game_functionality():
    """Test the current_game_id functionality"""
    db = SessionLocal()
    try:
        print("Testing current_game_id functionality...")
        
        # Get or create a test user
        test_user = db.query(User).filter(User.username == "test_user").first()
        if not test_user:
            test_user = User(username="test_user", password_hash="test_hash")
            db.add(test_user)
            db.commit()
            db.refresh(test_user)
            print(f"Created test user: {test_user.username} (ID: {test_user.id})")
        
        # Test 1: Check if user has no current game initially
        current_game = get_user_current_game(db, test_user.id)
        print(f"Test 1 - Initial current game: {current_game}")
        
        # Test 2: Start a new game and set it as current
        target_word = get_random_word(db)
        new_game = start_new_game(db, test_user.id, target_word.word)
        print(f"Test 2 - Started new game: {new_game.id}")
        
        # Test 3: Verify the game is set as current
        current_game = get_user_current_game(db, test_user.id)
        print(f"Test 3 - Current game after start: {current_game.id if current_game else None}")
        
        # Test 4: Clear current game
        clear_user_current_game(db, test_user.id)
        current_game = get_user_current_game(db, test_user.id)
        print(f"Test 4 - Current game after clear: {current_game}")
        
        # Test 5: Set specific game as current
        set_user_current_game(db, test_user.id, new_game.id)
        current_game = get_user_current_game(db, test_user.id)
        print(f"Test 5 - Current game after manual set: {current_game.id if current_game else None}")
        
        print("All tests passed! ✅")
        
    except Exception as e:
        print(f"Error testing current_game_id functionality: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_current_game_functionality()
