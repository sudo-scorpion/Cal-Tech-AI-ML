from app.models.cart import Cart, CartItem
from app.data.data_store import carts_db

def get_cart(session_id):
    if session_id not in carts_db:
        carts_db[session_id] = Cart(session_id)
    return carts_db[session_id]

def add_to_cart(session_id, product_id, quantity):
    cart = get_cart(session_id)
    cart.add_item(product_id, quantity)
    return cart.get_items()

def remove_from_cart(session_id, product_id):
    cart = get_cart(session_id)
    cart.remove_item(product_id)
    return cart.get_items()

def update_item_quantity(session_id, product_id, quantity):
    cart = get_cart(session_id)
    cart.update_quantity(product_id, quantity)
    return cart.get_items()

def get_cart_items(session_id):
    cart = get_cart(session_id)
    return cart.get_items()

def clear_cart(session_id):
    # Assuming carts_db is a dictionary mapping session_ids to Cart instances
    from app.data.data_store import carts_db  # Import here to avoid circular imports
    if session_id in carts_db:
        carts_db[session_id].items.clear()  # Clear the cart items for the given session_id
    return carts_db[session_id].get_items()  # Return the updated cart items

# Path: ShoppingApp/app/models/cart.py


