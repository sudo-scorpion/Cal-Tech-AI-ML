from flask import Blueprint, jsonify, request
from app.services.auth_services import login, logout

# Create a Blueprint object
auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['POST'])
def login_route():
    try:
        request_data = request.get_json()

        # Validate request data
        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400

        username = request_data.get('username')
        password = request_data.get('password')

        response, status_code = login(username, password)
        return response, status_code

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500
    
@auth_routes.route('/logout/<int:user_id>', methods=['POST'])
def logout_route(user_id):
    try:
        response, status_code = logout(user_id)
        return response, status_code

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500
    