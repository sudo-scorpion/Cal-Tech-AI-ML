from flask import Blueprint, jsonify, request, session 
from helper import requires_role
from user import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['POST'])
def register():
    try:
        request_data = request.get_json()

        # Validate request data
        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400

        response, status_code = User.register_user(request_data)
        print(User.users)
        print(User.user_roles)
        return response, status_code

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@user_routes.route('/login', methods=['POST'])
def login():
    try:
        request_data = request.get_json()

        # Validate request data
        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400

        response, status_code = User.login_user(request_data)

        if status_code == 200:  # Successful login
            username = response.get_json().get('username')
            session['username'] = username

        return response, status_code

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@user_routes.route('/user-update', methods=['PUT'])
@requires_role('user')
def user_update():
    try:
        request_data = request.get_json()

        # Validate request data
        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400

        response, status_code = User.update_user(request_data)
        print(User.users)
        print(User.user_roles)
        return response, status_code

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500
