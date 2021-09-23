FROM python:slim

RUN useradd microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN virtualenv -p python3 microblog_venv
RUN microblog_venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY config.py microblog.py ./
