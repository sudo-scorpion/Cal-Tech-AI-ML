from flask import Blueprint, jsonify, request 
from helper import requires_role
from product import Product

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/products/add', methods=['POST'])
@requires_role('admin')
def add_products_route():
    try:
        request_data = request.get_json()

        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        response, status_code = Product.add_product(request_data)

        return response, status_code
            
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@product_routes.route('/products/delete', methods=['DELETE'])
@requires_role('admin')
def delete_products_route():
    try:
        request_data = request.get_json()

        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        response, status_code = Product.delete_product(request_data)

        return response, status_code
            
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500
