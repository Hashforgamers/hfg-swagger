# Use the official Swagger UI image as the base
FROM swaggerapi/swagger-ui

# Disable the entrypoint script
RUN chmod -x /docker-entrypoint.d/40-swagger-ui.sh

# Set the default URL in Swagger UI to our OpenAPI file
ENV SWAGGER_JSON=/usr/share/nginx/html/swagger.json

# Copy the OpenAPI JSON file to the Swagger UI directory
COPY swagger.json /usr/share/nginx/html/swagger.json
