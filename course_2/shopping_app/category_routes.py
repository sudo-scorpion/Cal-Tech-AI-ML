from flask import Blueprint, jsonify, request 
from helper import requires_role
from category import Category

category_routes = Blueprint('category_routes', __name__)

@category_routes.route('/categories/add', methods=['POST'])
@requires_role('admin')
def add_categories_route():
    try:
        request_data = request.get_json()

        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        response, status_code = Category.add_category(request_data)

        return response, status_code
            
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@category_routes.route('/categories/delete', methods=['DELETE'])
@requires_role('admin')
def delete_categories_route():
    try:
        request_data = request.get_json()

        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        response, status_code = Category.add_category(request_data)

        return response, status_code
            
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500
