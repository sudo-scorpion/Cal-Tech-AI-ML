import hashlib
from flask import request, jsonify
from typing import List, Dict

class User:
    # Define users and user_roles as a class-level attribute
    users: Dict[str, str] = {}
    user_roles: Dict[str, List[str]] = {}

    @classmethod
    def assign_role(cls, username: str, role: str):
        if username in cls.user_roles:
            if role not in cls.user_roles[username]:
                cls.user_roles[username].append(role)
            else:
                print(f"User '{username}' already has the role '{role}")
        else:
            cls.user_roles[username] = [role]

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def validate_user(username, password):
        user_data = User.users.get(username)
        if user_data:
            stored_password = user_data.get('password')
            if stored_password:
                hashed_password = User.hash_password(password)
                if hashed_password == stored_password:
                    return True 
        return False

    @staticmethod
    def register_user(request_data):
        try:
            # Extract user data from request
            firstname = request_data.get('firstname')
            lastname = request_data.get('lastname')
            username = request_data.get('username')
            password = request_data.get('password')
            email = request_data.get('email')
            role = request_data.get('role')

            # Validate input
            if not all([firstname, lastname, username, password, email, role]):
                raise ValueError("Missing required fields")

            # Check if username already exists
            if username in User.users:
                return jsonify({'error': 'Username already exists'}), 400

            # Hash the password
            hashed_password = User.hash_password(password)

            # Register user
            User.users[username] = {
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'password': hashed_password,
                'email': email
            }

            for r in role: 
                User.assign_role(username, r)

            return jsonify({'message': 'User registered successfully', 'username': username}), 201

        except KeyError as e:
            return jsonify({'error': f'Missing required field: {e}'}), 400
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'An error occurred while registering user'}), 500
    
    @staticmethod
    def update_user(request_data):
        try:
            # Extract user data from request
            firstname = request_data.get('firstname')
            lastname = request_data.get('lastname')
            username = request_data.get('username')
            password = request_data.get('password')
            email = request_data.get('email')
            role = request_data.get('role')

            print(password)

            # Validate input
            if not all([username, password]):
                raise ValueError("Missing required fields: username and password")

            # Validate user credentials
            if not User.validate_user(username, password):
                return jsonify({'error': 'Invalid username or password'}), 401

            # Hash the password
            hashed_password = User.hash_password(password)

            # Retrieve current user data
            current_user = User.users.get(username)

            # Update user information
            if not firstname:
                firstname = current_user.get('firstname')
            if not lastname:
                lastname = current_user.get('lastname')
            if not email:
                email = current_user.get('email')
            if not role:
                role = User.user_roles.get(username, [])

            # Update user roles
            for r in role:
                User.assign_role(username, r)

            # Update user data
            User.users[username] = {
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'password': hashed_password,
                'email': email
            }

            return jsonify({'message': 'Updated user successfully', 'username': username}), 200

        except KeyError as e:
            return jsonify({'error': f'Missing required field: {e}'}), 400
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'An error occurred while updating user'}), 500

    @staticmethod
    def login_user(request_data):
        try:
            # Extract user login credentials from request
            username = request_data.get('username')
            password = request_data.get('password')

            if User.validate_user(username, password):
                print("Authentication successful")
                return jsonify({'message': 'User logged in  successfully', 'username': username}), 200
            else:
                print("Authentication failed")
                return jsonify({'error': 'Invalid username or password'}), 401
            
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {e}'}), 400
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'An error occurred while login user'}), 500
 
    

