from flask_restx import Namespace, Resource, fields, marshal_with
from app.services.checkout_service import process_checkout
from flask import session

# Define the namespace
checkout_ns = Namespace('checkout', description='Checkout related operations.')

# Model for checkout data
checkout_model = checkout_ns.model('Checkout', {
    'payment_method': fields.String(required=True, description='Payment method'),
    'payment_details': fields.Raw(required=True, description='Payment details such as card number, PayPal email, etc.'),
})

@checkout_ns.route('/')
class Checkout(Resource):
    @checkout_ns.expect(checkout_model)
    def post(self):
        """Process the checkout"""
        session_id = session.get('session_id')
        data = checkout_ns.payload
        result = process_checkout(session_id, data['payment_method'], data['payment_details'])
        if result.get('success'):
            return {'message': 'Checkout successful.', 'order_details': result}, 200
        else:
            return {'message': 'Checkout failed.', 'error': result.get('error')}, 400
