# FROM python:3.5-onbuild
FROM ubuntu:latest

MAINTAINER Brian Lusina "lusinabrian@gmail.com"

RUN apt-get update -y && apt-get install -y python-pip python-dev python3-pip

# setting up python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1

RUN update-alternatives --set python /usr/bin/python3.5

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app
# ADD . /app

# this will expose this app to other containers via port 8000
EXPOSE 8000

# ENTRYPOINT [ "python" ]

CMD ["python3", "manage.py", "runserver"]
