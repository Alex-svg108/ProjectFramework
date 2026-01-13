# Указываем базовый образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libpq-dev gcc git postgresql-client && \
    rm -rf /var/lib/apt/lists/*
RUN python -m pip install --upgrade pip

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt


# Копируем остальные файлы проекта в контейнер
COPY . /app

# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

# Определяем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
