from app.models.user import User
from app.mock_db.data_store import users
from flask import jsonify
from app.mock_db.data_store import users
from app.utils.helper_functions import hash_password

# User services
def create_user(request_data):
    if request_data:
        user_id = len(users) + 1
        username = request_data.get('username')
        password = request_data.get('password')
        email = request_data.get('email')
        user_role = request_data.get('user_role')
 
        # Check if all required fields are present
        if not all([username, password, email, user_role]):
            return jsonify({'error': 'Missing data'}), 400
        
        # Check if the username is already taken
        if username in [user.username for user in users.values()]:
            return jsonify({'error': 'Username already taken'}), 400
        
        user = User(user_id, username, hash_password(password), email, user_role)
        users[user.user_id] = user
        return jsonify({'message': 'User created successfully', 'user': user.__json__()}), 201

def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({'user': user.__json__()}), 200
    return jsonify({'error': 'User not found'}), 404

def get_all_users():
    all_users = [user.__json__() for user in users.values()]
    if all_users:
        return jsonify({'users': all_users}), 200
    return jsonify({'error': 'No users found'}), 404

def update_user(user_id, username=None, password=None, email=None, user_role=None):
    user = get_user(user_id)
    if user:
        if username:
            user.username = username
        if password:
            user.password =hash_password(password)
        if email:
            user.email = email
        if user_role:
            user.user_role = user_role
        return jsonify({'message': 'User updated successfully', 'user': user.__json__()}), 200

def delete_user(user_id):
    user = get_user(user_id)
    if user:
        del users[user_id]
        return jsonify({'message': 'User deleted successfully'}), 200
    return False