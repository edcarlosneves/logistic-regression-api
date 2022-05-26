FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN pip3 install -r /usr/src/app/requirements/development.txt

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]