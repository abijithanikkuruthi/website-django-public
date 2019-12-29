# Local Development

## Setup
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip3 install -r requirements.txt`

## Migrations
1. `python3 manage.py makemigrations`
2. `python3 manage.py migrate`

## Collect Static Files
`python3 manage.py collectstatic`

## Enable Debugging
`DEBUG=True` in `abijith/settings.py`

## Start Server
`python3 manage.py runserver`
