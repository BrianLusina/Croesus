FROM python:3.5-onbuild

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]