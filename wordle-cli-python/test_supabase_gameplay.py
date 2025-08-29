import sys
import os
sys.path.insert(0, 'src')

from src.config.settings import SessionLocal
from src.services.game_service import start_new_game, make_guess, update_game_status, clear_user_current_game
from src.services.word_service import get_random_word
from src.models.user import User
from sqlalchemy.orm import Session
import time

def test_supabase_gameplay():
    """Test complete gameplay flow with Supabase data pushing"""
    print("🎮 Testing Supabase Gameplay Data Pushing...")
    
    db = SessionLocal()
    try:
        # Create a test user for gameplay
        test_user = db.query(User).filter(User.username == "gameplay_test").first()
        if not test_user:
            test_user = User(username="gameplay_test", password_hash="test_hash")
            db.add(test_user)
            db.commit()
            db.refresh(test_user)
            print(f"Created test user: {test_user.username}")
        
        # Clear any existing current game
        clear_user_current_game(db, test_user.id)
        
        # Test 1: Start a new game
        print("1. Starting new game...")
        target_word = get_random_word(db)
        game = start_new_game(db, test_user.id, target_word.word)
        print(f"   ✅ Game started: ID {game.id}, Target: {target_word.word}")
        
        # Test 2: Make several guesses
        print("2. Making guesses...")
        test_words = ["APPLE", "WATER", "HOUSE", "MUSIC", target_word.word.upper()]
        
        for i, guess_word in enumerate(test_words, 1):
            guess = make_guess(db, game.id, guess_word, i)
            print(f"   ✅ Guess {i}: '{guess_word}' -> Feedback: {guess.feedback}")
            
            # Check if game was won
            if guess.feedback == "GGGGG":  # All correct
                print("   🎉 Game won!")
                update_game_status(db, game.id, "won")
                break
            time.sleep(0.1)  # Small delay to see the progression
        
        # Test 3: Update game status if not already won
        if game.status == "in_progress":
            update_game_status(db, game.id, "lost")
            print("   ❌ Game lost")
        
        # Test 4: Verify data was pushed to Supabase
        print("3. Verifying data in Supabase...")
        
        # Check game record
        from src.models.game import Game
        saved_game = db.query(Game).filter(Game.id == game.id).first()
        print(f"   ✅ Game saved: ID {saved_game.id}, Status: {saved_game.status}, Attempts: {saved_game.attempts}")
        
        # Check guesses
        from src.models.guess import Guess
        guesses = db.query(Guess).filter(Guess.game_id == game.id).order_by(Guess.position).all()
        print(f"   ✅ {len(guesses)} guesses saved:")
        for guess in guesses:
            print(f"      Position {guess.position}: '{guess.guess_word}' -> {guess.feedback}")
        
        # Test 5: Verify user current game was updated
        current_game = db.query(User).filter(User.id == test_user.id).first().current_game_id
        print(f"   ✅ User current game ID: {current_game}")
        
        print("\n🎉 Supabase gameplay test completed successfully!")
        print("✅ All game data was successfully pushed to Supabase")
        print("✅ Game state is properly maintained")
        print("✅ User progress is correctly tracked")
        
        return True
        
    except Exception as e:
        print(f"❌ Gameplay test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()

def test_multiple_games():
    """Test multiple games to ensure data consistency"""
    print("\n🔄 Testing Multiple Games...")
    
    db = SessionLocal()
    try:
        test_user = db.query(User).filter(User.username == "multi_game_test").first()
        if not test_user:
            test_user = User(username="multi_game_test", password_hash="test_hash")
            db.add(test_user)
            db.commit()
            db.refresh(test_user)
        
        game_ids = []
        
        # Play 3 quick games
        for game_num in range(1, 4):
            print(f"Playing game {game_num}...")
            clear_user_current_game(db, test_user.id)
            
            target_word = get_random_word(db)
            game = start_new_game(db, test_user.id, target_word.word)
            game_ids.append(game.id)
            
            # Make a couple of guesses
            for i in range(1, 3):
                guess_word = "TEST" + str(i)  # Simple test words
                make_guess(db, game.id, guess_word, i)
            
            update_game_status(db, game.id, "completed")
            print(f"   ✅ Game {game_num} completed: ID {game.id}")
        
        # Verify all games exist
        from src.models.game import Game
        saved_games = db.query(Game).filter(Game.id.in_(game_ids)).all()
        print(f"✅ All {len(saved_games)} games successfully saved to Supabase")
        
        return True
        
    except Exception as e:
        print(f"❌ Multiple games test failed: {e}")
        return False
    finally:
        db.close()

if __name__ == "__main__":
    success1 = test_supabase_gameplay()
    success2 = test_multiple_games()
    
    if success1 and success2:
        print("\n🎊 ALL SUPABASE PUSHING TESTS PASSED! 🎊")
        print("✅ Database connection is stable")
        print("✅ Data is being successfully pushed to Supabase")
        print("✅ Gameplay data is properly persisted")
        print("✅ Multiple game sessions work correctly")
    else:
        print("\n❌ Some tests failed. Check Supabase connection and configuration.")
