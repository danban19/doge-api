"""Entry point for the FastAPI application."""
import os
import requests

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def read_root():
    """Endpoint to check the health of the application."""
    return {"status": "ok"}

@app.get("/breeds/")
def get_breeds(limit: int = 10, page: int = 0):
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
    return response.json()


@app.get("/breeds/{breed_id}")
def get_breed(breed_id: str):
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
    return response.json()
