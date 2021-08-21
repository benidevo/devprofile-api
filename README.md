# devprofile-api

This is the backend service for a mobile application that enables recruiters to easily find and hire software developers 


## Technologies 

The following technologies were used in this project:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)


## Requirements

Before starting, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

Kindly ensure that you are in the root directory before running the following commands.

## Create a virtual environment

    python3 -m venv env

## Activate the virtual environment

    . env/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Navigate to the source directory

    cd src

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Run Tests

    python manage.py test

## Start server

    python manage.py runserver
