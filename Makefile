prod_run:
	poetry run gunicorn studfood.wsgi

run:
	poetry run python manage.py runserver