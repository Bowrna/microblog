#syntax=docker/dockerfile:1
FROM python:slim

RUN useradd microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN python -m venv microblog_venv
RUN microblog_venv/bin/pip install -r requirements.txt
RUN microblog_venv/bin/pip install cryptography pymysql

COPY app app
COPY migrations migrations
COPY config.py microblog.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
