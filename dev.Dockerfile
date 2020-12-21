FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /usr/src/app/
COPY requirements-dev.txt /usr/src/app/

RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements-dev.txt

ADD . /usr/src/app