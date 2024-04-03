from flask import jsonify
from app.models.cart import Cart
from app.mock_db.data_store import carts

# Cart services
def create_cart(user_id, session_id, product_id, quantity):
    try:
        cart_id = len(carts) + 1
        if not all([user_id, session_id, product_id, quantity]):
            return jsonify({"error": "All fields are required"}), 400
        cart_item = Cart(cart_id, user_id, session_id, product_id, quantity)
        carts[cart_id] = cart_item
        return jsonify({'message': 'Cart created successfully', 'cart': cart_item.__json__()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_cart(cart_id):
    try:
        if not cart_id:
            return jsonify({"error": "Cart ID is required"}), 400
        item = carts.get(cart_id)
        if item:
            return jsonify({'cart': item.__json__()}), 200
        return jsonify({"error": "Cart not found"}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
def get_all_carts():
    try:
        all_carts = [item.__json__() for item in carts.values()]
        if not all_carts:
            return jsonify({"error": "No carts found"}), 404
        return jsonify({'carts': all_carts}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def update_cart(cart_id, user_id=None, session_id=None, product_id=None, quantity=None):
    try:
        if not cart_id:
            return jsonify({"error": "Cart ID is required"}), 400
        item = carts.get(cart_id)
        if not item:
            return jsonify({"error": "Cart not found"}), 404
        if user_id:
            item.user_id = user_id
        if session_id:
            item.session_id = session_id
        if product_id:
            item.product_id = product_id
        if quantity:
            item.quantity = quantity
        return jsonify({'message': 'Cart updated successfully', 'cart': item.__json__()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def delete_cart(cart_id):
    try:
        if not cart_id:
            return jsonify({"error": "Cart ID is required"}), 400
        del carts[cart_id]
        return jsonify({'message': 'Cart deleted successfully'}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
