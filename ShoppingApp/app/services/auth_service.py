from werkzeug.security import generate_password_hash, check_password_hash
from app.data.data_store import users_db
from app.models import User

def add_user(username, email, password, role='customer'):
    user_id = len(users_db) + 1
    hashed_password = generate_password_hash(password)
    new_user = User(user_id, username, email, hashed_password, role, session_id=None)
    users_db.append(new_user)
    return new_user

def authenticate_user(username, password):
    user = next((u for u in users_db if u.username == username), None)
    if user and check_password_hash(user.password, password):
        return user
    return None
