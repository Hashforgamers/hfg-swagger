# Start from the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files into the container
COPY ./api /app

# Install necessary dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose Flask's default port (5000)
EXPOSE 5000

# Install Nginx to serve Swagger UI if needed
RUN apt-get update && apt-get install -y nginx

# Copy the Swagger UI files into the container (optional, if serving locally)
COPY ./swagger /usr/share/nginx/html/swagger

# Add a custom Nginx config file (optional, if you're serving Swagger UI through Nginx)
COPY ./nginx.conf /etc/nginx/nginx.conf

# Run both Flask and Nginx (as a single process or using a process manager like Supervisor)
CMD ["sh", "-c", "service nginx start && python app.py"]
