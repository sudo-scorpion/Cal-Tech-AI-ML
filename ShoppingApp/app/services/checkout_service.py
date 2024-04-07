from app.services.cart_service import get_cart_items, clear_cart
from app.data.data_store import orders_db  # Ensure this exists in data_store.py
from app.data.data_store import products_db  # Ensure this exists in products.py

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
    elif payment_method == 'CreditCard':
        # Simplified payment validation
        if 'card_number' not in payment_details:
            return {'success': False, 'error': 'Invalid credit card number'}
        print(f"Processing Credit Card payment for {payment_details['card_number']}")
        # Normally, you'd integrate with a payment gateway API here
    else:
        return {'success': False, 'error': 'Invalid payment method'}
    
    # For simplicity, assume payment is always successful
    
    total_amount = 0
    items = []

    for item in cart_items:
        product_id = item.product_id
        quantity = item.quantity

        # Find the product in the products database
        product = next((p for p in products_db if int(p.id) == int(product_id)), None)

        if product:
            name = product.name
            price = float(product.price)
            total_amount += price * float(quantity)
            items.append({'product_id': product_id, 'name': name, 'price': price, 'quantity': quantity})
        else:
            return {'success': False, 'error': f'Product with ID {product_id} not found'}

    order_id = create_order_record(session_id, items)
    clear_cart(session_id)  # Clear the cart after successful checkout

    return {'success': True, 'order_id': order_id, 'total': total_amount, 'items': items}

def create_order_record(session_id, items):
    order_id = len(orders_db) + 1  # Generate a new order ID
    order = {'order_id': order_id, 'session_id': session_id, 'items': items}
    orders_db.append(order)
    return order_id
