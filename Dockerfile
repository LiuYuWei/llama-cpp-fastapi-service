# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Set working directory to /app
WORKDIR /app

# Update and upgrade system packages, then install essential build tools
# Clean up in the same RUN instruction to avoid caching unnecessary files
RUN apt update && apt -y upgrade \
    && apt install -y --no-install-recommends build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages
# First copy only the requirements.txt to ensure we don't invalidate the Docker cache 
# when other files change
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the FastAPI application files to the container
COPY ./app /app

# Expose port 8000 for FastAPI
EXPOSE 8000

# Start the FastAPI application using UVicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
