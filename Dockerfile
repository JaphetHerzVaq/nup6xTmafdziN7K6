# syntax=docker/dockerfile:1

# Base Python image, using slim variant for minimal size
ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim AS base

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define working directory
WORKDIR /app

# Install system dependencies required for pytesseract, OpenCV, and other tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    tesseract-ocr \
    tesseract-ocr-eng \
    libtesseract-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Install pip and upgrade it
RUN pip install --upgrade pip

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt --timeout 100

# Create necessary folders with appropriate permissions
RUN mkdir -p /app/upload /app/process /app/static && \
    chmod -R 777 /app/upload /app/process /app/static

# Copy the source code into the container
COPY . /app

# Expose the port on which the Flask app will run
EXPOSE 3000

# Command to run the application
CMD ["python", "image-ocr-test.py"]


