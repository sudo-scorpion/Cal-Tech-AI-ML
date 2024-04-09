import os
import time
import hashlib
from functools import wraps
from flask import request, session
from app.data.data_store import users_db
from app.data.data_store import products_db
from utils.bypass_role_requirements import check_bypass_flag
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def generate_secure_id(user_identifier):
    # Ensure user_identifier is a string. If it's not, you can convert it.
    user_identifier = str(user_identifier).encode('utf-8')
    # Generate random data for additional entropy
    random_data = os.urandom(64)
    # Get the current timestamp
    timestamp = str(time.time()).encode('utf-8')
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    # Update the hash object with the random data, timestamp, and user-specific information
    hash_object.update(random_data)
    hash_object.update(timestamp)
    hash_object.update(user_identifier)
    # Return the hexadecimal representation of the digest
    return hash_object.hexdigest()

# Decorator to verify a user doesn't exist
def ensure_user_does_not_exist(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = request.get_json()
        if data:
            username = data.get('username')
            email = data.get('email')
        if not username or not email:
            return {'error': 'Username and email are required'}, 400
        if any(user.username == username or user.email == email for user in users_db):
            return {'error': 'User already exists'}, 400
        return func(*args, **kwargs)
    return wrapper
# Decorator to require specific roles
def requires_roles(*required_roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            print('Bypassing role requirements: ', check_bypass_flag())
            if check_bypass_flag():
                return fn(*args, **kwargs)
            if 'role' and 'session_id' not in session:
                # Assuming unauthenticated users don't have a 'user_role' key in the session
                return {'error': 'Authentication required'}, 401
            role = session['role']
            session_id = session['session_id']
            print(f"Role: {role}, Session ID: {session_id}")
            if role not in required_roles or session_id is None:
                return {'error': 'Unauthorized'}, 403
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# Decorator to valid admin token
def requires_admin_token(fn):
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if 'admin_token' not in request.json:
            return {'error': 'Admin token required'}, 403
        admin_token = request.json.get('admin_token')
        if admin_token != os.getenv('ADMIN_TOKEN'):
            return {'error': 'Invalid admin token'}, 403
        return fn(*args, **kwargs)
    return decorated_view

# Decorator to ensure product exists
# {'session id': 'session 5', 'items': [{'product_id': 2, 'quantity': 1}, {'product_id': 7, 'quantity': 1}]}
def ensure_product_exists(fn):
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        data = request.get_json()
        if data:
            items = data.get('items')
            if items:
                for item in items:
                    product_id = item.get('product_id')
                    if not any(product.id == product_id for product in products_db):
                        return {'error': 'Product not found'}, 404
        return fn(*args, **kwargs)
    return decorated_view

