web: gunicorn src.core.wsgi
release: cd src && python manage.py makemigrations --noinput
release: cd src && python manage.py collectstatic --noinput
release: cd src && python manage.py migrate --noinput
