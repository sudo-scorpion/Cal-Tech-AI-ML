import os
import time
import hashlib
from functools import wraps
from flask import jsonify, request, session
from app.models.product import Product


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

def requires_roles(*required_roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if 'user_role' not in session:
                # Assuming unauthenticated users don't have a 'user_role' key in the session
                return jsonify({'error': 'Authentication required'}), 401
            user_role = session['user_role']
            if user_role not in required_roles:
                return jsonify({'error': 'Unauthorized'}), 403
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


# # # Authorization decorator
# def requires_role(role):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if 'username' not in session or role not in User.user_roles.get(session['username'], []):
#                 return jsonify({'error': 'Unauthorized access'}), 403
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

# Decorator to ensure product ID exists
def ensure_product_exists(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(request.get_json())
        request_data = request.get_json();
        if request_data:
            product_id = request_data.get('products').get('product_id')
        if product_id is None:
            return jsonify({'error': 'Product ID is missing from cart data'}), 400
        if product_id not in Product.products:
            return jsonify({'error': 'Product not found'}), 404
        return func(*args, **kwargs)
    return wrapper