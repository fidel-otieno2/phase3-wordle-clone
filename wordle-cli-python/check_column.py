import sys
sys.path.insert(0, 'src')
from src.config.settings import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        # Check if current_game_id column already exists
        result = conn.execute(text("SELECT column_name FROM information_schema.columns WHERE table_name = 'users' AND column_name = 'current_game_id';"))
        column_exists = result.fetchone()
        if column_exists:
            print('current_game_id column already exists in users table')
        else:
            print('current_game_id column does not exist in users table')
except Exception as e:
    print(f'Error checking column: {e}')
