from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Path to swagger.json (this assumes it's located in the /app/swagger folder)
SWAGGER_JSON = 'swagger/swagger.json'

# Set up Swagger UI Blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',  # The URL path to access Swagger UI
    SWAGGER_JSON,  # The path to the swagger.json file in the container
    config={
        'app_name': "My Flask API"
    }
)

# Register the Swagger UI blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix='/swagger')

# Serve the raw swagger.json (optional)
@app.route('/swagger.json')
def swagger_json():
    return send_from_directory('swagger', 'swagger.json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Ensure Flask listens on all interfaces
