from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..config.settings import Base

class User(Base):
    """User model for storing player information and authentication"""
    
    _tablename_ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
    current_game_id = Column(Integer, ForeignKey('games.id'), nullable=True)  # Track ongoing game
    
    # Relationships
    games = relationship("Game", back_populates="user", cascade="all, delete-orphan", foreign_keys="Game.user_id")
    
    def _repr_(self):
        return f"<User(id={self.id}, username='{self.username}')>"