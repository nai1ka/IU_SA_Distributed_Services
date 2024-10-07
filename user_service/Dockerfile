FROM python:3.9-slim

WORKDIR /app

COPY ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY user_service /app/user_service
COPY config.py /app/config.py

WORKDIR /app/user_service

CMD ["python", "app.py"]