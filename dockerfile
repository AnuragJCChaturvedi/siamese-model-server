# Use an official Python runtime as a base image
FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libhdf5-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    pkg-config \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "app.py"]
