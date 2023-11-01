prod_run:
	poetry run gunicorn studfood.wsgi

run:
	poetry run python manage.py runserver

test:
	poetry run pytest --cov

lint:
	poetry run mypy .
	poetry run ruff .

migrate:
	poetry run python manage.py migrate

