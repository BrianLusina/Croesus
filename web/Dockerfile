# FROM python:3.5-onbuild
FROM ubuntu:latest

MAINTAINER Brian Lusina "lusinabrian@gmail.com"

RUN apt-get update -y && apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
# ADD . /app

# ENTRYPOINT [ "python" ]

CMD ["python", "manage.py", "runserver"]
