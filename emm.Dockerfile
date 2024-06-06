FROM python:3.10-slim

WORKDIR /app

ENV PIP_NO_CACHE_DIR=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install -U pip setuptools wheel
COPY fwk/requirements.emm.txt .
RUN pip install -r requirements.emm.txt

COPY fwk .
