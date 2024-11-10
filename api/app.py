from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# External URL for the swagger.json file
API_URL = 'https://hfg-swagger.onrender.com/swagger.json'

# Set up Swagger UI Blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',  # The URL path to access Swagger UI
    API_URL,  # External URL for the swagger.json file
    config={
        'app_name': "My Flask API"
    }
)

# Register the Swagger UI blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix='/swagger')

# Serve the raw swagger.json (optional, in case you need to serve it locally too)
@app.route('/swagger.json')
def swagger_json():
    return send_from_directory('swagger', 'swagger.json')  # Optional: serve it locally

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)  # Specify port=5050
