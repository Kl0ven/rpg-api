FROM python:3.8-slim

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/images
WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libpq-dev python-dev gcc libcairo2 tzdata \
    && rm -rf /var/lib/apt/lists/* 

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN apt-get purge -y --auto-remove gcc

VOLUME [ "/usr/src/app/images" ]

EXPOSE 8080
ENV MODE=PRODUCTION
ENV TZ Europe/Paris

ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:8080", "rpg_api.__main__:app"]