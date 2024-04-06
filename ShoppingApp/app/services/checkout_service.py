from app.services.cart_service import get_cart_items, clear_cart
from app.data.data_store import orders_db  # Ensure this exists in data_store.py

def process_checkout(session_id, payment_method, payment_details):
    cart_items = get_cart_items(session_id)
    if not cart_items:
        return {'success': False, 'error': 'Cart is empty'}

    # Simulate payment processing
    if payment_method == 'PayPal':
        # Simplified payment validation
        if 'email' not in payment_details:
            return {'success': False, 'error': 'Invalid PayPal email'}
        print(f"Processing PayPal payment for {payment_details['email']}")
        # Normally, you'd integrate with PayPal API here

    # For simplicity, assume payment is always successful
    order_id = create_order_record(session_id, cart_items)
    clear_cart(session_id)  # Clear the cart after successful checkout
    return {'success': True, 'order_id': order_id, 'items': cart_items}

def create_order_record(session_id, cart_items):
    order_id = len(orders_db) + 1  # Generate a new order ID
    order = {'order_id': order_id, 'session_id': session_id, 'items': cart_items}
    orders_db.append(order)
    return order_id
