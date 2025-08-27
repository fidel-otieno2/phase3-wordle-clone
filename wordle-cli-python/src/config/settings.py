from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from urllib.parse import quote_plus

# Database configuration - Choose between SQLite (development) and PostgreSQL (production)
DATABASE_TYPE = os.getenv("DATABASE_TYPE", "sqlite")  # Default to sqlite for development

if DATABASE_TYPE == "postgresql":
    # PostgreSQL configuration for Supabase
    # Replace these values with your actual Supabase credentials
    DB_USERNAME = os.getenv("DB_USERNAME", "postgres.szfyytdzcgljaesbwkri")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "CQ9A4@Axf?Hw-Z6")
    DB_HOST = os.getenv("DB_HOST", "aws-1-eu-north-1.pooler.supabase.com")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "postgres")
    
    # URL-encode the password to handle special characters
    encoded_password = quote_plus(DB_PASSWORD)
    SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USERNAME}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    # Create PostgreSQL engine
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
else:
    # SQLite configuration for development
    SQLALCHEMY_DATABASE_URL = "sqlite:///./wordle.db"
    
    # Create SQLite engine
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, 
        connect_args={"check_same_thread": False}
    )

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
