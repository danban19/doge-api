"""Module containing the SQLAlchemy models for the database."""
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for the SQLAlchemy models."""


class BreedSQLModel(Base):
    """SQL Model for the breeds table."""
    __tablename__ = 'breeds'
    db_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id = Column(Integer, index=True)
    name = Column(String)
    country_code = Column(String)
    bred_for = Column(String)
    breed_group = Column(String)
    life_span = Column(String)
    temperament = Column(String)
    origin = Column(String)
    reference_image_id = Column(String)
    weight = Column(JSON)
    height = Column(JSON)
    image = Column(JSON)
