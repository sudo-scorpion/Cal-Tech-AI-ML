from flask import Blueprint, jsonify, request
from app.services.cart_services import get_all_carts, get_cart, create_cart, update_cart, delete_cart

cart_routes = Blueprint('cart_routes', __name__)

@cart_routes.route('/carts/<int:cart_id>', methods=['GET'])
def get_cart_route(cart_id):
    try:
        if not cart_id:
            return jsonify({"error": "Cart ID is required"}), 400
        response, status_code = get_cart(cart_id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500

@cart_routes.route('/carts', methods=['GET'])
def get_all_carts_route():
    try:
        response, status_code = get_all_carts()
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500
    
@cart_routes.route('/carts', methods=['POST'])
def create_cart_route():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        session_id = data.get('session_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        if not all([user_id, session_id, product_id, quantity]):
            return jsonify({"error": "All fields are required"}), 400
        
        response, status_code = create_cart(user_id, session_id, product_id, quantity)
        return response, status_code
    
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500

@cart_routes.route('/carts/<int:cart_id>', methods=['PUT'])
def update_cart_route(cart_id):
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        session_id = data.get('session_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        if not all([user_id, session_id, product_id, quantity]):
            return jsonify({"error": "All fields are required"}), 400
        
        response, status_code = update_cart(cart_id, user_id, session_id, product_id, quantity)
        return response, status_code
    
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500
    
@cart_routes.route('/carts/<int:cart_id>', methods=['DELETE'])
def delete_cart_route(cart_id):
    try:
        response, status_code = delete_cart(cart_id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500
