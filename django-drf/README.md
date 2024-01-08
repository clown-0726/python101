#### common commands

```
python manage.py createsuperuser
python manage.py makemigrations [app]
python manage.py migrate

django-admin startproject myblog
python manage.py startapp blog
python manage.py runserver 9999
python manage.py inspectdb --database=postgres > login/models.py

# Get random secret key
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Check security level with using below command 
python manage.py check --deploy

# Collect static files
python manage.py collectstatic

# local test with gunicorn
gunicorn --env DJANGO_SETTINGS_MODULE=server.settings -b :8080 --chdir ./ server.wsgi -w 4 --log-level=debug --pid ./gunicorn.pid
```
