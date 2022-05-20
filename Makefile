SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )


runserver:
	python manage.py runserver

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

create-super-user:
	python manage.py createsuperuser

test:
	python manage.py test

lint:
	pylint project/ 

style:
	black .
