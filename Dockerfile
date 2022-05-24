FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN pip3 install -r /usr/src/app/requirements/development.txt

EXPOSE 8080

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]