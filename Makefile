SHELL := /bin/bash # Use bash syntax
ARG := $(word 2, $(MAKECMDGOALS) )


docker-compose-up:
	docker-compose up -d

docker-compose-stop:
	docker-compose stop

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
