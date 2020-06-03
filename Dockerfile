FROM python:3.8-alpine

RUN apk add --no-cache --update \
    build-base \
    postgresql-dev \
    bash \
    && rm -rf /var/cache/apk/*

RUN mkdir /app/
WORKDIR /app/

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt