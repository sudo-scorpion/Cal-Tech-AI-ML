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
# Boots, Coats, Jackets, and Caps are added to the categories_db
categories_db = [
    Category(id = 1, name = "Boots"),
    Category(id = 2, name = "Coats"),
    Category(id = 3, name = "Jackets"),
    Category(id = 4, name = "Caps"),
]

# Products
# Add more products to the products_db using these -  Boots, Coats, Jackets, and Cap
# Let's 20 items of total 5 products each with a price of 100.0

products_db = [
    Product(id=1, name='Timberland Boots', price=1200.99, category_id=1),
    Product(id=2, name='North Face Coat', price=1500.99, category_id=2),
    Product(id=3, name='Leather Jacket', price=1000.99, category_id=3),
    Product(id=4, name='Baseball Cap', price=15.99, category_id=4),
    Product(id=5, name='Beanie', price=10.99, category_id=4),
    Product(id=6, name='Bucket Hat', price=20.99, category_id=4),
    Product(id=7, name='Cowboy Boots', price=1500.99, category_id=1),
    Product(id=8, name='Rain Coat', price=1200.99, category_id=2),
    Product(id=9, name='Bomber Jacket', price=1000.99, category_id=3),
    Product(id=10, name='Hiking Boots', price=2000.99, category_id=1),
    Product(id=11, name='Winter Coat', price=1800.99, category_id=2),
    Product(id=12, name='Denim Jacket', price=900.99, category_id=3),
    Product(id=13, name='Snapback Cap', price=25.99, category_id=4),
    Product(id=14, name='Visor', price=12.99, category_id=4),
    Product(id=15, name='Fedora Hat', price=30.99, category_id=4),
    Product(id=16, name='Chelsea Boots', price=1400.99, category_id=1),
    Product(id=17, name='Trench Coat', price=1100.99, category_id=2),
    Product(id=18, name='Parka Jacket', price=950.99, category_id=3),
    Product(id=19, name='Trucker Cap', price=18.99, category_id=4),
    Product(id=20, name='Bucket Hat', price=22.99, category_id=4),
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
