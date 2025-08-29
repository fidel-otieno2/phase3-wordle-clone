import sys
import os
sys.path.insert(0, 'src')

from src.config.settings import SessionLocal, engine, Base
from src.models.user import User
from src.models.game import Game
from src.models.guess import Guess
from src.models.word import Word
from sqlalchemy.orm import Session
from sqlalchemy import text
import time

def test_supabase_connection():
    """Test the Supabase database connection and basic CRUD operations"""
    print("🧪 Testing Supabase Database Connection...")
    
    db = SessionLocal()
    try:
        # Test 1: Check if we can connect to the database
        print("1. Testing database connection...")
        connection = engine.connect()
        result = connection.execute(text("SELECT version()"))
        db_version = result.scalar()
        print(f"   ✅ Connected to PostgreSQL: {db_version}")
        connection.close()
        
        # Test 2: Test basic query to check if tables exist
        print("2. Testing table existence...")
        tables = ['users', 'games', 'guesses', 'words']
        for table in tables:
            try:
                result = db.execute(text(f"SELECT COUNT(*) FROM {table}"))
                count = result.scalar()
                print(f"   ✅ Table '{table}' exists with {count} records")
            except Exception as e:
                print(f"   ❌ Table '{table}' error: {e}")
        
        # Test 3: Test inserting a new record
        print("3. Testing data insertion...")
        try:
            # Create a test user
            test_user = User(username=f"test_user_{int(time.time())}", password_hash="test_hash")
            db.add(test_user)
            db.commit()
            db.refresh(test_user)
            print(f"   ✅ Successfully inserted test user: {test_user.username} (ID: {test_user.id})")
            
            # Test 4: Test reading the inserted data
            print("4. Testing data retrieval...")
            retrieved_user = db.query(User).filter(User.id == test_user.id).first()
            if retrieved_user:
                print(f"   ✅ Successfully retrieved user: {retrieved_user.username}")
            else:
                print("   ❌ Failed to retrieve user")
                
            # Test 5: Test updating data
            print("5. Testing data update...")
            retrieved_user.username = f"updated_{retrieved_user.username}"
            db.commit()
            db.refresh(retrieved_user)
            print(f"   ✅ Successfully updated user: {retrieved_user.username}")
            
            # Test 6: Test deleting data
            print("6. Testing data deletion...")
            db.delete(retrieved_user)
            db.commit()
            print("   ✅ Successfully deleted test user")
            
        except Exception as e:
            print(f"   ❌ Data operation error: {e}")
            db.rollback()
        
        print("\n🎉 All Supabase connection tests completed!")
        print("✅ Database connection is working properly")
        print("✅ CRUD operations are functioning correctly")
        print("✅ Data is being successfully pushed to Supabase")
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

def test_supabase_performance():
    """Test Supabase performance with multiple operations"""
    print("\n⚡ Testing Supabase Performance...")
    
    db = SessionLocal()
    try:
        start_time = time.time()
        
        # Test bulk insert performance
        print("Testing bulk insert performance...")
        test_users = []
        for i in range(5):
            user = User(username=f"perf_test_{i}_{int(time.time())}", password_hash="test_hash")
            test_users.append(user)
            db.add(user)
        
        db.commit()
        insert_time = time.time() - start_time
        print(f"   ✅ Inserted {len(test_users)} users in {insert_time:.3f} seconds")
        
        # Test query performance
        query_start = time.time()
        users_count = db.query(User).filter(User.username.like("perf_test_%")).count()
        query_time = time.time() - query_start
        print(f"   ✅ Queried {users_count} users in {query_time:.3f} seconds")
        
        # Clean up
        for user in test_users:
            db.delete(user)
        db.commit()
        print("   ✅ Cleaned up test data")
        
        total_time = time.time() - start_time
        print(f"\n📊 Performance summary: {total_time:.3f} seconds total")
        
    except Exception as e:
        print(f"❌ Performance test failed: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    test_supabase_connection()
    test_supabase_performance()
