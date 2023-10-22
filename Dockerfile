FROM python:3.11-slim

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем pip
RUN set -x \
    && apt-get update \
    && apt-get -y install sudo && apt-get -y update \
    && sudo apt-get update -y && pip install --upgrade pip \
    && apt-get autoremove --purge -y && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Копируем список требуемых библиотек
COPY ./requirements.txt /code/requirements.txt

# Устанавливаем требуемые библиотеки
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
