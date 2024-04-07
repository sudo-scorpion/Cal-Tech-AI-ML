from flask_restx import Namespace, Resource, fields
from flask import session
from utils.helper import requires_roles
from app.services.cart_service import add_to_cart, remove_from_cart, get_cart_items, update_item_quantity

# Define the namespace
cart_ns = Namespace('cart', description='Cart related operations.')

# Model for cart item data
cart_item_model = cart_ns.model('CartItem', {
    'product_id': fields.Integer(required=True, description='The product identifier'),
    'quantity': fields.Integer(required=True, description='Quantity of the product'),
})

# Model for adding or updating cart items
cart_action_model = cart_ns.model('CartAction', {
    'product_id': fields.Integer(required=True, description='The product identifier'),
    'quantity': fields.Integer(required=True, description='Quantity of the product'),
})

@cart_ns.route('/')
class CartList(Resource):
    @cart_ns.doc('list_cart')
    @cart_ns.marshal_list_with(cart_item_model, code=200)
    @requires_roles('user')
    def get(self):
        """List all items in the cart"""
        session_id = session.get('session_id')
        print(session_id)
        return get_cart_items(session_id), 200

    @cart_ns.expect(cart_action_model)
    @cart_ns.marshal_with(cart_item_model, code=201)
    @requires_roles('user')
    def post(self):
        """Add an item to the cart"""
        session_id = session.get('session_id')
        data = cart_ns.payload
        for item in data['items']:
            add_to_cart(session_id, item['product_id'], item['quantity'])
        return get_cart_items(session_id), 201

@cart_ns.route('/<int:product_id>')
@cart_ns.param('product_id', 'The product identifier')
@cart_ns.response(404, 'Item not found in cart')
class CartItem(Resource):
    @cart_ns.doc('delete_item_from_cart')
    @cart_ns.response(204, 'Item removed from cart')
    @cart_ns.marshal_with(cart_action_model, code=201)
    @requires_roles('user')
    def delete(self, product_id):
        """Remove an item from the cart"""
        session_id = session.get('session_id')
        return remove_from_cart(session_id, product_id)

    @cart_ns.expect(cart_action_model)
    @cart_ns.marshal_with(cart_item_model, code=200)
    @requires_roles('user')
    def put(self, product_id):
        """Update an item's quantity in the cart"""
        session_id = session.get('session_id')
        data = cart_ns.payload
        return update_item_quantity(session_id, product_id, data['quantity']), 200
