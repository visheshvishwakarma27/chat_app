release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn project.wsgi 
release: ./release-tasks.sh
