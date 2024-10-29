"""Database connection and session management."""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "".join(
    [
        "postgresql://",
        os.environ.get("DB_USER", "postgres"),
        ":",
        os.environ.get("DB_PASSWORD", "postgres"),
        "@",
        f"{os.environ.get('DB_HOST', 'localhost')}:{os.environ.get('DB_PORT', '5432')}",
        "/",
        os.environ.get("DB_NAME", None)
    ]
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

Base = declarative_base()
Base.metadata.create_all(engine)

def get_db():
    """Function to get the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()