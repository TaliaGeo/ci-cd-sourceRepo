
FROM python:3.11-slim

WORKDIR /app

COPY app.py .
COPY inventory.csv .
COPY requirements.txt .
COPY templates/ templates/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
