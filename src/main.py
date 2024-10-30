"""Entry point for the FastAPI application."""
import os
import requests

from fastapi import FastAPI
import polars as pl

from db.client import Base, engine, session
from db.db_models import BreedSQLModel
from response_models import BreedResponseModel, BreedListResponseModel

app = FastAPI()

# Create tables on startup
@app.on_event("startup")
def on_startup():
    """"Startup event to create tables in the database."""
    Base.metadata.create_all(bind=engine)


@app.get("/health")
async def read_root():
    """Endpoint to check the health of the application."""
    return {"status": "ok"}

@app.get("/breeds/")
async def get_breeds(limit: int = 10, page: int = 0) -> BreedListResponseModel:
    """Endpoint to get all breeds from The Dog API.
    https://developers.thecatapi.com/view-account/ylX4blBYT9FaoVd6OhvR?report=bOoHBz-8t
    Args:
        limit (int): Number of breeds to return.
        page (int): Page number to return.
    Returns:
        dict: JSON response from The Dog API.
    """
    base_url = os.getenv("DOG_API_BASE_URL")
    headers = {
        "x-api-key": os.getenv("DOG_API_KEY")
    }
    url = f"{base_url}/breeds?limit={limit}&page={page}"
    response = requests.get(url, headers=headers)
    breeds = response.json()

    return BreedListResponseModel(breeds=breeds)


@app.get("/breeds/{breed_id}")
async def get_breed(breed_id: str) -> BreedResponseModel:
    """Endpoint to get a breed by ID from The Dog API.
    Args:
        breed_id (str): ID of the breed to return.
    Returns:
        dict: JSON response from The Dog API.
    """
    base_url = os.getenv("DOG_API_BASE_URL")
    headers = {
        "x-api-key": os.getenv("DOG_API_KEY")
    }
    url = f"{base_url}/breeds/{breed_id}"
    response = requests.get(url, headers=headers)

    # Save the breed to the database
    data = response.json()
    df = pl.DataFrame([data])

    for row in df.to_dicts():
        db_breed = BreedSQLModel(**row)
        session.add(db_breed)

    session.commit()

    return BreedResponseModel(**data)


@app.get("/browsed-breeds")
async def get_saved_breeds() -> BreedListResponseModel:
    """Endpoint to get all the previously browsed breeds from the database.
    Returns:
        dict: JSON response from the database.
    """
    breeds = session.query(BreedSQLModel).all()
    breeds_dict = [breed.__dict__ for breed in breeds]

    return BreedListResponseModel(breeds=breeds_dict)
