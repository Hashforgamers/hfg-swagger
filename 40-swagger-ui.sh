#!/bin/sh
# /docker-entrypoint.d/40-swagger-ui.sh

# Check if swagger.json already exists before trying to copy
if [ ! -f /usr/share/nginx/html/swagger.json ]; then
  cp /swagger.json /usr/share/nginx/html/swagger.json
else
  echo "swagger.json already exists, skipping copy"
fi
