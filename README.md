# doge-api
An API to retrieve data about dog breeds. Uses external API called "The Dog API".
To get more info about the external API, explore the following documentation:
https://developers.thecatapi.com/view-account/ylX4blBYT9FaoVd6OhvR?report=bOoHBz-8t

### Python version
The API uses Python 3.12.7 version. Use pyenv to install it according to this tutorial: https://realpython.com/intro-to-pyenv/

### Install poetry
Use the following link and follow the instructions to install Poetry: https://python-poetry.org/docs/

### Install Docker
https://docs.docker.com/engine/install/

### Install PostgreSQL
sudo apt install postgresql postgresql-contrib

In case of issues with PostgreSQL dependencies: sudo apt-get install libpq-dev

### Install dependencies
cd src
poetry install


### Activate virtual environment
poetry shell

### Start PostgreSQL server
docker compose up

### Run server
uvicorn main:app --reload --env-file .env
