# pull official base image
FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG DJANGO_ALLOWED_HOSTS
ARG DJANGO_SECRET_KEY
ARG DJANGO_CORS_ORIGIN_WHITELIST

ENV DJANGO_ALLOWED_HOSTS $DJANGO_ALLOWED_HOSTS
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY
ENV DJANGO_CORS_ORIGIN_WHITELIST $DJANGO_CORS_ORIGIN_WHITELIST

WORKDIR /backend
COPY requirements.txt /backend/

RUN apk add postgresql-dev libressl-dev libffi-dev gcc musl-dev gcc python3-dev musl-dev zlib-dev jpeg-dev #--(5.2)

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /backend/
