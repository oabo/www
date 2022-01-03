# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install flask redis  flask_bootstrap flask_nav requests

COPY . .

CMD [ "python3", "/app/www/main.py"]

