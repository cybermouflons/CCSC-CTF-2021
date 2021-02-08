#!/bin/sh

# echo "Waiting for postgres..."

# while ! nc -z web-db 5432; do
#   sleep 0.1
# done

# echo "PostgreSQL started"

pipenv run python manage.py create-db
pipenv run python manage.py create-data
pipenv run python manage.py run -h 0.0.0.0
