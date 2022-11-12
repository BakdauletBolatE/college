# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add -u postgresql-dev gcc python3-dev musl-dev  zlib-dev jpeg-dev build-base


COPY ./reqiurements.txt ./reqiurements.txt

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r reqiurements.txt

# copy project
COPY . .