# website-django

## Setup
python3 -m venv venv
source venv/bin/activate
pip3 -r install requirements.txt

## Migrations
python3 manage.py makemigrations
python3 manage.py migrate

## Collect Static Files
python3 manage.py collectstatic

## Start Server
python3 manage.py runserver
