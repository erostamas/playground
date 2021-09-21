FROM ubuntu:latest
MAINTAINER Tamas Eros (tamas.eros1@gmail.com)

RUN apt-get update --allow-unauthenticated --fix-missing
RUN apt-get install -y python3 \
                       python3-pip \
                       curl \
                       wget

RUN pip install flask

ADD erostamas_rest_service.py /usr/bin/

WORKDIR /

ENTRYPOINT /usr/bin/erostamas_rest_service.py
