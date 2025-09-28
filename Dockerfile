FROM python:3.12-slim

WORKDIR /app

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN pip install uvicorn[standard]
ARG LIBS
RUN pip install ${LIBS}

COPY fwk .
