FROM python:3.11.13-alpine3.22

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY manage_inventory.py .
COPY inventory.csv .
COPY templates/ ./templates/

EXPOSE 8080
FROM python:3.11.13-alpine3.22

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY manage_inventory.py .
COPY inventory.csv .
COPY templates/ ./templates/

EXPOSE 8080

CMD sh -c "python manage_inventory.py && python app.py"

