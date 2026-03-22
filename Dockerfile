FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files to /app
COPY . .

# Ensure /app is in PYTHONPATH
ENV PYTHONPATH="/app:${PYTHONPATH}"
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

EXPOSE 8000

# Start the ADK agent. We use '.' to scan the current directory (/app)
CMD ["sh", "-c", "adk web . --host 0.0.0.0 --port $PORT"]
