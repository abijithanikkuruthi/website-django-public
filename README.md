# Local Development

## Setup
  `python3 -m venv venv`
  `source venv/bin/activate`
  `pip3 install -r requirements.txt`

## Migrations
  `python3 manage.py makemigrations`
  `python3 manage.py migrate`

## Collect Static Files
`python3 manage.py collectstatic`

## Enable Debugging
`DEBUG=True` in `abijith/settings.py`

## Start Server
`python3 manage.py runserver`
