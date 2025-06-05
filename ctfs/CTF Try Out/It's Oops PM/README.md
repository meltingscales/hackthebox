# It's Oops PM

## Start the database

    docker compose up -d

## Setup venv

    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt

## Gather data

    python3 gather_data.py