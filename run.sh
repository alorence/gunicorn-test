#!/usr/bin/env bash

source venv/bin/activate

python manage.py migrate

gunicorn --bind unix:/var/tmp/gunicorn_tests.sock -c ./config/gunicorn.py  gunicorn_https.wsgi:application
