#!/bin/sh

python manage.py collectstatic --noinput
Pyehon manage.py makemigrations
python manage.py migrate
gunicorn config.wsgi --bind=0.0.0.0:80

