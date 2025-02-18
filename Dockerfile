FROM python:3.13-slim-bookworm
WORKDIR /app
RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN adduser --system --no-create-home app
USER app
ENTRYPOINT ["python", "main.py"]