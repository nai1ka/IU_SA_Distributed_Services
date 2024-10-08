FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY feed_service /app/feed_service
COPY config.py /app/config.py
COPY models.py /app/models.py

WORKDIR /app/feed_service

CMD ["python", "app.py"]