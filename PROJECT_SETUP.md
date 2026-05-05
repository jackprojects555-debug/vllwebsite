# Project Setup

## Python Version
Python 3.14.4

## Framework
Django 6.0.4

## CMS
Wagtail 7.3.1

## Database
PostgreSQL (psycopg 3.3.4)

## Deployment
Render (planned)

## Environment

Create virtual environment:

python3 -m venv .venv

Activate:

source .venv/bin/activate

## Installed Packages (current environment)

Django 6.0.4  
Wagtail 7.3.1  
psycopg 3.3.4  
gunicorn 26.0.0  
whitenoise 6.12.0  
python-dotenv 1.2.2  

## Run

After Django project initialization:

Apply migrations:

python manage.py migrate

Create admin user:

python manage.py createsuperuser

Run development server:

python manage.py runserver