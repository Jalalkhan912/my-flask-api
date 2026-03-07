# Start from an official slim Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy and install dependencies first (leverages Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]