FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/mpdatabase

COPY Pipfile Pipfile.lock /code/mpdatabase/
RUN pip install pipenv && pipenv install --system
COPY . /code/mpdatabase/