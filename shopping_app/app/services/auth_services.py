from app.models.user import User
from app.models.session import Session
from app.mock_db.data_store import users, sessions
from flask import jsonify, session as flask_session
from app.utils.helper_functions import generate_secure_id, hash_password
import datetime

def login(username, password):
    try:
        user = next((user for user in users.values() if user.username == 
                     username and user.password == hash_password(password)), None)
        if user:
            session_id = generate_secure_id(user.username)
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            session = Session(session_id, user.user_id, timestamp, True)
            user.session_id = session_id
            sessions[session_id] = session
            flask_session['username'] = user.username # Session maintained by Flask
            flask_session['user_id'] = user.user_id
            flask_session['user_role'] = user.user_role            
            return jsonify({'message': 'Login successful', 'user': user.__json__()}), 200
        return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500
    
def logout(user_id):
    try:
        user = users.get(user_id)
        session = sessions.get(user.session_id)
        if user and session.is_active == True:
            session.is_active = False
            session.logout_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            session.session_id = None
            flask_session.pop(user.username, None)
            flask_session.pop(user.user_id, None)
            flask_session.pop(user.user_role, None)
            return jsonify({'message': 'Logout successful'}), 200
        return jsonify({'error': 'User not found or logged in'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500
