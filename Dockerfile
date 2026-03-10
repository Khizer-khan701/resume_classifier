# Use Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=resume_classifier_project.settings.prod \
    PORT=7860 \
    REDIS_URL=redis://localhost:6379/0

# Set work directory
WORKDIR /app

# Install system dependencies including redis-server
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    redis-server \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Make the start script executable
COPY start-hf.sh /app/start-hf.sh
RUN chmod +x /app/start-hf.sh

# Expose port (Hugging Face uses 7860)
EXPOSE 7860

# Run the start script
CMD ["/app/start-hf.sh"]
