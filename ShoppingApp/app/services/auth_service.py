from werkzeug.security import generate_password_hash, check_password_hash
from app.data.data_store import users_db
from app.models import User
from utils.helper import generate_secure_id
from flask import session

def add_user(username, email, password, role='user'):
    user_id = len(users_db) + 1
    hashed_password = generate_password_hash(password)
    new_user = User(user_id, username, email, hashed_password, role, session_id=None)
    users_db.append(new_user)
    return new_user

def authenticate_user(username, password):
    user = next((u for u in users_db if u.username == username), None)
    if user and check_password_hash(user.password, password):
        user.session_id = generate_secure_id(user.id)
        session['session_id'] = user.session_id
        session['role'] = user.role
        return user
    return None

def logout_user():
    session.pop('session_id', None)
    session.pop('role', None)

def get_all_users():
    return users_db
