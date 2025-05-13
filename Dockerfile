# Создаем образ на основе Python версии 3.11-slim
FROM python:3.11-slim

# Задаем рабочую директорию
WORKDIR /code

# Запрещаем Python записывать .pyc файлы и отключаем буферизацию вывода
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

# Копируем список требуемых библиотек Python
COPY ./requirements.txt /code/requirements.txt

# Обновляем пакетный менеджер, устанавливаем pip и требуемые библиотеки
RUN set -x && \
    apt-get update && \
    apt-get -y install sudo && apt-get -y update && \
    sudo apt-get update -y && pip install --upgrade pip && \
    apt-get autoremove --purge -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
	pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Добавляем приложение в контейнер
ADD ./app /code/app
