FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY analysis/ ./analysis/
COPY predictions/ ./predictions/
COPY data/ ./data/
COPY runner.py .

CMD ["python3", "runner.py"]
