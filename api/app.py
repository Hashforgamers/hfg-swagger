from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Define the external URL for the swagger.json file
SWAGGER_JSON_URL = 'https://hfg-swagger.onrender.com/swagger.json'  # Change this to your external URL
SWAGGER_JSON = 'https://hfg-swagger.onrender.com/swagger.json' 

# Set up Swagger UI Blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',  # The URL path to access Swagger UI
    #SWAGGER_JSON_URL,  # External URL for the swagger.json file
    SWAGGER_JSON,
    config={
        'app_name': "My Flask API"
    }
)

# Register the Swagger UI blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix='/swagger')

# Serve the raw swagger.json (optional, in case you need to serve it locally too)
@app.route('/swagger.json')
def swagger_json():
    return send_from_directory('swagger', 'swagger.json')  # If you want to serve it locally

if __name__ == '__main__':
    app.run(debug=True)
