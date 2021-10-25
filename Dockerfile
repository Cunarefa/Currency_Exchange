FROM python:3.7-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/CurrencyExchange

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY . CurrencyExchange/
COPY ./requirements.txt app

WORKDIR CurrencyExchange

RUN pip install -r requirements.txt
