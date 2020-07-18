FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /filestoreservice

ADD . /filestoreservice

COPY ./requirements.txt /filestoreservice/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py makemigrations

RUN python manage.py migrate
