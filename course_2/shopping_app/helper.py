from functools import wraps
from flask import jsonify, session
from user import User

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
