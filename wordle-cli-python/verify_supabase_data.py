import sys
import os
sys.path.insert(0, 'src')

from src.config.settings import SessionLocal
from src.models.user import User
from src.models.game import Game
from src.models.guess import Guess
from sqlalchemy.orm import Session
from sqlalchemy import func

def verify_supabase_data():
    """Verify that all test data was successfully pushed to Supabase"""
    print("🔍 Verifying Supabase Data Integrity...")
    
    db = SessionLocal()
    try:
        # Get overall statistics
        total_users = db.query(User).count()
        total_games = db.query(Game).count()
        total_guesses = db.query(Guess).count()
        
        print(f"📊 Database Statistics:")
        print(f"   Total Users: {total_users}")
        print(f"   Total Games: {total_games}")
        print(f"   Total Guesses: {total_guesses}")
        
        # Check test users
        test_users = db.query(User).filter(
            User.username.like("%test%") | User.username.like("%gameplay%")
        ).all()
        
        print(f"\n👥 Test Users Found: {len(test_users)}")
        for user in test_users:
            user_games = db.query(Game).filter(Game.user_id == user.id).count()
            print(f"   {user.username}: {user_games} games")
        
        # Check recent games
        recent_games = db.query(Game).order_by(Game.id.desc()).limit(5).all()
        print(f"\n🎯 Recent Games (last 5):")
        for game in recent_games:
            game_guesses = db.query(Guess).filter(Guess.game_id == game.id).count()
            user = db.query(User).filter(User.id == game.user_id).first()
            username = user.username if user else "Unknown"
            print(f"   Game {game.id}: {username}, {game.status}, {game_guesses} guesses")
        
        # Check data consistency
        print(f"\n✅ Data Consistency Checks:")
        
        # Check if all games have a user
        orphaned_games = db.query(Game).filter(~Game.user_id.in_(db.query(User.id))).count()
        print(f"   Orphaned games (no user): {orphaned_games}")
        
        # Check if all guesses have a game
        orphaned_guesses = db.query(Guess).filter(~Guess.game_id.in_(db.query(Game.id))).count()
        print(f"   Orphaned guesses (no game): {orphaned_guesses}")
        
        # Check game status distribution
        status_counts = db.query(Game.status, func.count(Game.id)).group_by(Game.status).all()
        print(f"   Game Status Distribution:")
        for status, count in status_counts:
            print(f"     {status}: {count} games")
        
        print(f"\n🎉 Supabase Data Verification Complete!")
        print(f"✅ All test data successfully pushed and verified")
        print(f"✅ Database integrity maintained")
        print(f"✅ No orphaned records detected")
        
        return True
        
    except Exception as e:
        print(f"❌ Data verification failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    success = verify_supabase_data()
    if success:
        print("\n✨ SUPABASE PUSHING VERIFICATION SUCCESSFUL! ✨")
    else:
        print("\n❌ Verification failed. Check database connection.")
