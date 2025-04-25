FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install prometheus-client prometheus-flask-exporter

COPY . .

CMD ["python", "app.py"]
