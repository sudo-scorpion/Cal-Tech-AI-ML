from app.models.payment import Payment
from app.mock_db.data_store import payments
from flask import jsonify

# Payment services
def create_payment(user_id, amount, payment_method, payment_status):
    try:
        payment_id = len(payments) + 1
        if not all([user_id, amount, payment_method, payment_status]):
            return jsonify({"error": "All fields are required"}), 400
        payment = Payment(payment_id, user_id, amount, payment_method, payment_status)
        payments[payment_id] = payment
        return jsonify({'message': 'Payment created successfully', 'payment': payment.__json__()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_payment(payment_id):
    try:
        if not payment_id:
            return jsonify({"error": "Payment ID is required"}), 400
        payment = payments.get(payment_id)
        if payment:
            return jsonify({'payment': payment.__json__()}), 200
        return jsonify({"error": "Payment not found"}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_all_payments():
    try:
        all_payments = [payment.__json__() for payment in payments.values()]
        if not all_payments:
            return jsonify({"error": "No payments found"}), 404
        return jsonify({'payments': all_payments}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_payment(payment_id, user_id=None, amount=None, payment_method=None, payment_status=None):
    try:
        if not payment_id:
            return jsonify({"error": "Payment ID is required"}), 400
        payment = payments.get(payment_id)
        if not payment:
            return jsonify({"error": "Payment not found"}), 404
        if user_id:
            payment.user_id = user_id
        if amount:
            payment.amount = amount
        if payment_method:
            payment.payment_method = payment_method
        if payment_status:
            payment.payment_status = payment_status
        return jsonify({'message': 'Payment updated successfully', 'payment': payment.__json__()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_payment(payment_id):
    try:
        if not payment_id:
            return jsonify({"error": "Payment ID is required"}), 400
        payment = payments.get(payment_id)
        if not payment:
            return jsonify({"error": "Payment not found"}), 404
        del payments[payment_id]
        return jsonify({'message': 'Payment deleted successfully'}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
