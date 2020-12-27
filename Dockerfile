FROM python:3.8-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libpq-dev python-dev gcc \
    && rm -rf /var/lib/apt/lists/* 

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN apt-get purge -y --auto-remove gcc

EXPOSE 8080
ENV MODE=PRODUCTION

ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:8080", "rpg_api.__main__:app"]