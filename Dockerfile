ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /bot

COPY ./pyproject.toml .
COPY ./poetry.lock .
COPY ./requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY . .

ENTRYPOINT python bot/bot.py
