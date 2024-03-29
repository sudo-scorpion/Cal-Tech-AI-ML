import os
import binascii
import hashlib
from typing import List, Dict
from functools import wraps
from flask import Flask, request, jsonify, session, redirect, url_for
from user import User

app = Flask(__name__)
app.secret_key = binascii.hexlify(os.urandom(24)).decode() 

# Authorization decorator
def requires_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'username' not in session or role not in User.user_roles.get(session['username'], []):
                return jsonify({'error': 'Unauthorized access'}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
    }
    .container {
        max-width: 800px;
        margin: 50px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #333;
        text-align: center;
    }
    </style>
    </head>
    <body>
    <div class="container">
        <h1>Welcome to the Demo Marketplace</h1>
    </div>
    </body>
    </html>
    """

@app.route('/register', methods=['POST'])
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

@app.route('/login', methods=['POST'])
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

@app.route('/user-update', methods=['PUT'])
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
    
@app.route('/admin', methods=['GET'])
@requires_role('admin')
def admin_page():
    return jsonify({'message': 'Welcome to the admin page'})

if __name__ == '__main__':
    app.run(debug=True)