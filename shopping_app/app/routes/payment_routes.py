from flask import Blueprint, jsonify, request
from app.services.payment_services import get_payment, get_all_payments, create_payment, update_payment, delete_payment

payment_routes = Blueprint('payment_routes', __name__)

@payment_routes.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment_route(payment_id):
    try:
        if not payment_id:
            return jsonify({"error": "Payment ID is required"}), 400
        response, status_code = get_payment(payment_id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500

@payment_routes.route('/payments', methods=['GET'])
def get_all_payments_route():
    try:
        print("get_all_payments_route")
        response, status_code = get_all_payments()
        print(response, status_code)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500   

@payment_routes.route('/payments', methods=['POST'])
def create_payment_route():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        amount = data.get('amount')
        payment_method = data.get('payment_method')
        payment_status = data.get('payment_status')

        if not all([user_id, amount, payment_method, payment_status]):
            return jsonify({"error": "All fields are required"}), 400
        
        response, status_code = create_payment(user_id, amount, payment_method, payment_status)
        return response, status_code
    
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500

@payment_routes.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment_route(payment_id):
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        amount = data.get('amount')
        payment_method = data.get('payment_method')
        payment_status = data.get('payment_status')

        if not all([user_id, amount, payment_method, payment_status]):
            return jsonify({"error": "All fields are required"}), 400
        
        response, status_code = update_payment(payment_id, user_id, amount, payment_method, payment_status)
        return response, status_code
    
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500
    
@payment_routes.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment_route(payment_id):
    try:
        if not payment_id:
            return jsonify({"error": "Payment ID is required"}), 400
        response, status_code = delete_payment(payment_id)
        return response, status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500