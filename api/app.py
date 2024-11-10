from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/vendor/<int:vendor_id>/documents', methods=['GET'])
def get_vendor_documents(vendor_id):
    """
    This endpoint retrieves the documents for a vendor
    ---
    parameters:
      - name: vendor_id
        in: path
        type: integer
        required: true
        description: The ID of the vendor
    responses:
      200:
        description: List of documents
        schema:
          type: array
          items:
            type: string
    """
    # Sample response (you can replace with actual logic)
    return {"documents": ["doc1", "doc2"]}

@app.route('/api/vendor/<int:vendor_id>/dashboard', methods=['GET'])
def get_vendor_dashboard(vendor_id):
    """
    This endpoint retrieves the dashboard for a vendor
    ---
    parameters:
      - name: vendor_id
        in: path
        type: integer
        required: true
        description: The ID of the vendor
    responses:
      200:
        description: Vendor dashboard data
        schema:
          type: object
          properties:
            total_revenue:
              type: integer
            active_sessions:
              type: integer
    """
    # Sample response (you can replace with actual logic)
    return {
        "total_revenue": 10000,
        "active_sessions": 50
    }

if __name__ == "__main__":
    app.run(debug=True)
