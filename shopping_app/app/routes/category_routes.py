from flask import Blueprint, jsonify, request
from app.services.category_services import get_category, get_all_categories, create_category, update_category, delete_category
from app.utils.helper_functions import requires_permission

category_routes = Blueprint('category_routes', __name__)

@category_routes.route('/categories', methods=['GET'])
def get_all_categories_route():
    try:
        return get_all_categories()
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})

@category_routes.route('/categories/<int:category_id>', methods=['GET'])
def get_category_route(category_id):
    try:
        if not category_id:
            return jsonify({'error': 'Category ID is required'}), 400
        
        response, status_code = get_category(category_id)
        return response, status_code   
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)}) 
 
    
@category_routes.route('/categories', methods=['POST'])
@requires_permission('add_category')
def create_category_route():
    try: 
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Category name is required'}), 400
        
        category_name = data.get('category_name')
        if not category_name:
            return jsonify({'error': 'Category name is required'}), 400
        
        response, status_code = create_category(category_name)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})

@category_routes.route('/categories/<int:category_id>', methods=['PUT'])
def update_category_route(category_id):
    try:
        if not category_id:
            return jsonify({'error': 'Category ID is required'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Category name is required'}), 400
        
        category_name = data.get('category_name')
        if not category_name:
            return jsonify({'error': 'Category name is required'}), 400
        
        response, status_code = update_category(category_id, category_name)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})
    
@category_routes.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category_route(category_id):
    try: 
        if not category_id:
            return jsonify({'error': 'Category ID is required'}), 400
        
        response, status_code = delete_category(category_id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)}) 
