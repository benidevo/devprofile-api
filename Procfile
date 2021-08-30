web: gunicorn src.core.wsgi --log-file -
release: cd src && python manage.py collectstatic 
release: cd src && python manage.py makemigrations
release: cd src && python manage.py migrate