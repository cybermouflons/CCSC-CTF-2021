#!/bin/sh

poetry run python manage.py create-db
poetry run python manage.py run -h 0.0.0.0
