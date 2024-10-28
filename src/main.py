"""Entry point for the FastAPI application."""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Example endpoint returning a JSON object."""
    return {"Hello": "World"}
