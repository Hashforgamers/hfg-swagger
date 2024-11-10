# Use the official Swagger UI image as the base
FROM swaggerapi/swagger-ui

# Set the default URL in Swagger UI to our OpenAPI file
ENV SWAGGER_JSON=/usr/share/nginx/html/swagger.json
