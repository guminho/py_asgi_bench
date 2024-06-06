FROM python:3.10-slim

WORKDIR /app

ENV PIP_NO_CACHE_DIR=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install -U pip setuptools wheel
COPY fwk/requirements.txt .
RUN pip install -r requirements.txt

COPY fwk .
