from app.models.session import Session
from app.mock_db.data_store import sessions
from flask import jsonify
from app.utils.helper_functions import generate_secure_id

# Session services
def create_session(request_data):
    try:
        session_id = generate_secure_id()
        user_id = request_data.get('user_id')
        timestamp = request_data.get('timestamp')
        is_active = request_data.get('is_active')

        session = Session(session_id, user_id, timestamp, is_active)
        sessions[session.session_id] = session
        return jsonify({'message': 'Session created successfully', 'session': sessions.get(session_id).__json__()}), 201
    except Exception as e:
        return {'error': 'An error occurred while processing the request'}, 500

def get_session(session_id):
    try:
        session = sessions.get(session_id)
        if session:
            return jsonify({'message': 'Session retrieved successfully', 'session': session.__json__()}), 200
        return None
    except Exception as e:
        return {'error': 'An error occurred while processing the request'}, 500
    
def get_all_sessions():
    try:
        return jsonify({'sessions': [session.__json__() for session in sessions.values()]}), 200
    except Exception as e:
        return {'error': 'An error occurred while processing the request'}, 500

def update_session(session_id, user_id=None, timestamp=None, is_active=None):
    session = get_session(session_id)
    if session:
        if user_id:
            session.user_id = user_id
        if timestamp:
            session.timestamp = timestamp
        if is_active:
            session.is_active = is_active

def delete_session(session_id):
    session = get_session(session_id)
    if session:
        sessions.remove(session)