from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.config.settings import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String, name='password_hash')

    current_game_id = Column(Integer, ForeignKey('games.id'), nullable=True)  # Add this line
    games = relationship("Game", back_populates="user", foreign_keys="[Game.user_id]")
