FROM python:3.7-slim

WORKDIR /usr/src/CurrencyExchange

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY . app/
COPY ./requirements.txt app

WORKDIR app

RUN pip install -r requirements.txt
