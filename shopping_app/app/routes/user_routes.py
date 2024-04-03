from flask import Blueprint, jsonify, request
from app.services.user_services import get_all_users, get_user, create_user, update_user, delete_user

# Create a Blueprint object
user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    try:
        if not user_id:
            return jsonify({'error': 'User ID is required'}), 400
        
        response, status_code = get_user(user_id)
        return response, status_code
    
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@user_routes.route('/users', methods=['GET'])
def get_all_users_route():
    try:
        response, status_code = get_all_users()
        return response, status_code

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500
    
@user_routes.route('/users', methods=['POST'])
def create_user_route():
    try:
        request_data = request.get_json()

        # Validate request data
        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400

        response, status_code = create_user(request_data)
        return response, status_code

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500


@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    try:
        request_data = request.get_json()

        # Validate request data
        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400

        response, status_code = update_user(user_id, request_data)
        return response, status_code

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    try:
        response, status_code = delete_user(user_id)
        return response, status_code

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500