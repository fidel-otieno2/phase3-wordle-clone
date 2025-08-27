from sqlalchemy.orm import Session
from src.models.user import User
import bcrypt

def create_user(db: Session, username: str, password: str):
    """Create a new user with hashed password"""
    # Hash the password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Create user instance
    user = User(username=username, password_hash=password_hash)
    
    # Add to database
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

def get_or_create_test_user(db: Session):
    """Get existing test user or create one if it doesn't exist"""
    # Try to find existing test user
    test_user = db.query(User).filter(User.username == "test_user").first()
    
    if not test_user:
        # Create test user
        test_user = create_user(db, "test_user", "test_password")
        print(f"Created test user with ID: {test_user.id}")
    else:
        print(f"Using existing test user with ID: {test_user.id}")
    
    return test_user