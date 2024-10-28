# doge-api
An API to retrieve data about dog breeds. Uses external API called "The Dog API".
To get more info about the external API, explore the following documentation:
https://developers.thecatapi.com/view-account/ylX4blBYT9FaoVd6OhvR?report=bOoHBz-8t

# Python version
The API uses Python 3.12.7 version. Use pyenv to install it according to this tutorial: https://realpython.com/intro-to-pyenv/

# Install poetry
Use the following link and follow the instructions to install Poetry: https://python-poetry.org/docs/

# Install dependencies
cd src
poetry install

# Activate virtual environment
poetry shell

# Run server
uvicorn main:app --reload --env-file .env
