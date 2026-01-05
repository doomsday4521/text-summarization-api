FROM python:3.12-slim

WORKDIR /app

# system deps (minimal)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copy dependencies first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
