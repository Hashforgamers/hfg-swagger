from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Path to your swagger.json
SWAGGER_JSON = '/app/swagger/swagger.json'

# Swagger UI blueprint configuration
swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',  # The URL path to access Swagger UI
    SWAGGER_JSON,  # The local path to swagger.json inside the container
    config={
        'app_name': "My Flask API"
    }
)

# Register the Swagger UI blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix='/swagger')

# Optionally, serve the raw swagger.json
@app.route('/swagger.json')
def swagger_json():
    return send_from_directory('/app/swagger', 'swagger.json')

if __name__ == '__main__':
    app.run(debug=True)
