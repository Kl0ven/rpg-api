FROM python:3.8-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y libpq-dev python-dev libcairo2 tzdata
RUN apt-get install -y --no-install-recommends gcc 

COPY requirements.txt /usr/src/app/
COPY requirements-dev.txt /usr/src/app/

RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements-dev.txt

RUN rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove gcc

ENV TZ Europe/Paris

ADD . /usr/src/app