from flask import Blueprint, jsonify, request
from app.services.product_services import get_product, get_all_products, create_product, update_product, delete_product

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/products', methods=['GET'])
def get_all_products_route():
    try:
        return get_all_products()
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})

@product_routes.route('/products/<int:product_id>', methods=['GET'])
def get_product_route(product_id):
    try:
        if not product_id:
            return jsonify({'error': 'Product ID is required'}), 400
        
        response, status_code = get_product(product_id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})

@product_routes.route('/products/add', methods=['POST'])
def create_product_route():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Product name, category ID and price are required'}), 400
        
        product_name = data.get('product_name')
        category_id = data.get('category_id')
        price = data.get('price')
        if not product_name or not category_id or not price:
            return jsonify({'error': 'Product name, category ID and price are required'}), 400
        
        response, status_code = create_product(product_name, category_id, price)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})

@product_routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    try:
        if not product_id:
            return jsonify({'error': 'Product ID is required'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Product name, category ID and price are required'}), 400
        
        product_name = data.get('product_name')
        category_id = data.get('category_id')
        price = data.get('price')
        if not product_name and not category_id and not price:
            return jsonify({'error': 'Product name, category ID and price are required'}), 400
        
        response, status_code = update_product(product_id, product_name, category_id, price)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})
    
@product_routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    try:
        if not product_id:
            return jsonify({'error': 'Product ID is required'}), 400
        
        response, status_code = delete_product(product_id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})