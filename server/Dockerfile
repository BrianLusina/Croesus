# FROM python:3.5-onbuild
FROM ubuntu:latest

MAINTAINER Brian Lusina "lusinabrian@gmail.com"

# install pip and python deps along with supervisor
RUN apt-get update -y && apt-get install -y python-pip python-dev python3-pip supervisor

# install supervisord
# RUN apt-get update -y && apt-get install -y supervisor

# setting up python alternatives
# setting python3.5 with a priority of 2, the higher the priority the better
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1

# set python 3.5 as default
RUN update-alternatives --set python /usr/bin/python3.5

# add code to application
ADD . /app
# COPY . /app

# set the working directory
WORKDIR /app

# install requirements
RUN pip3 install -r requirements.txt

# We copy just the requirements.txt first to leverage Docker cache
# COPY ./requirements.txt /app/requirements.txt

# this will expose this app to other containers via port 8000
EXPOSE 8000

# needs to be set else Celery gives an error (because docker runs commands inside
# container as root)
ENV C_FORCE_ROOT=1
# TODO: set other environment variables from .env file to docker container

# starts up server application
# CMD ["python3", "manage.py", "runserver"]

# run supervisord, command to use when starting this container
# CMD ["/usr/bin/supervisord"]