# Start from the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files into the container
COPY ./api /app

# Install necessary dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Install Flask-Swagger-UI to serve the Swagger UI
RUN pip install flask-swagger-ui

# Expose Flask's default port (5000)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
