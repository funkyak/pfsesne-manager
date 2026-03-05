# DCM Pfsense APT Manager - Docker Image
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY dcm_pfsense_apt_manager/ ./dcm_pfsense_apt_manager/
COPY main.py web.py ./

# Create data directory
RUN mkdir -p /data

# Environment
ENV PYTHONUNBUFFERED=1
ENV DCM_DATA_DIR=/data

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/api/status', auth=('admin', 'admin'))" || exit 1

CMD ["python", "web.py"]
