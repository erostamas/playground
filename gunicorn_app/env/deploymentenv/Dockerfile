FROM ubuntu:latest

RUN apt-get update --allow-unauthenticated --fix-missing
RUN apt-get install -y python3 \
                       python3-pip \
                       curl \
                       wget

RUN pip install flask

ADD erostamas_gunicorn_app.py /usr/bin/

WORKDIR /
