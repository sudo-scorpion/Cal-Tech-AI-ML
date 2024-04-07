###############################################################################.
# Description: This file contains the data store for the ShoppingApp. 
# It contains dummy data for users, categories, products, carts, and orders. 
# This data is used to simulate the behavior of the application during 
# development and testing
###############################################################################.

from app.models.product import Product
from app.models.category import Category
from app.models.cart import Cart, CartItem

# Users
users_db = []

# Categories
categories_db = [
    Category(id=1, name='Electronics'),
    Category(id=2, name='Books'),
]

# Products
products_db = [
    Product(id=1, name='Laptop', category_id=1, price=1200.99),
    Product(id=2, name='Science Fiction Book', category_id=2, price=15.99),
]

# Adjusted Carts with an explicit `items` argument
carts_db = {
    'session123': Cart(session_id='session123', items=[
        CartItem(product_id=1, quantity=1),
        CartItem(product_id=2, quantity=3),
    ]),
}

# Orders
orders_db = [
    # Assuming an order structure similar to Cart but with an order ID
    {'order_id': 1, 'session_id': 'session123', 'items': carts_db['session123'].get_items(), 'total_cost': 1200.99 + (15.99 * 3)}
]
