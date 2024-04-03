from flask import Blueprint, jsonify, request
from app.services.session_services import create_session, delete_session, get_all_sessions, get_session

# Create a Blueprint object
session_routes = Blueprint('session_routes', __name__)

# Define your routes
@session_routes.route('/sessions', methods=['POST'])
def create_session_route():
    try:
        request_data = request.get_json()

        # Validate request data
        if not request_data:
            return jsonify({'error': 'No JSON data received'}), 400

        response, status_code = create_session(request_data)
        return response, status_code
  
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@session_routes.route('/sessions', methods=['DELETE'])
def end_session_route():
    if delete_session():
        return jsonify({'message': 'Session ended'}), 200
    else:
        return jsonify({'error': 'No session to end'}), 404

@session_routes.route('/sessions/<string:session_id>', methods=['GET'])
def get_session_route(session_id):
    try:
        # Validate request data
        if not session_id:
            return jsonify({'error': 'No session ID provided'}), 400
        
        response, status_code = get_session(session_id)
        return response, status_code
    
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@session_routes.route('/sessions', methods=['GET'])
def get_all_sessions_route():
    try:
        response, status_code = get_all_sessions()
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request'}), 500
    
