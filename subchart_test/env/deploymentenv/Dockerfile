FROM ubuntu:latest
MAINTAINER Tamas Eros (tamas.eros1@gmail.com)

RUN apt-get update --allow-unauthenticated --fix-missing
RUN apt-get install -y python3

ADD main.py /opt/erostamas/subchart_test/

WORKDIR /
