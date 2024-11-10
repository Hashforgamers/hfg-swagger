# Start from the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY ./api /app

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
