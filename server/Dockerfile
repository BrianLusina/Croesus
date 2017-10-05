FROM python:3.6.1-onbuild

MAINTAINER Brian Lusina "lusinabrian@gmail.com"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# this will expose this app to other containers via port 8000
EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "manage.py", "runserver" ]