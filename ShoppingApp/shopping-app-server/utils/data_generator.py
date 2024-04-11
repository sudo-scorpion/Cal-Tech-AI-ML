import requests
import argparse
from bypass_role_requirements import clear_bypass_flag, set_bypass_flag

# Base URL of your Flask application
BASE_URL = 'http://localhost:5000'  # Update with your actual base URL

# Define function to generate dummy users
def generate_users():
    users_data = [
        {'username': 'john_doe', 'email': 'john@example.com', 'password': 'hash1'},
        {'username': 'jane_doe', 'email': 'jane@example.com', 'password': 'hash2', 'role': 'admin'},
        {'username': 'alice_smith', 'email': 'alice@example.com', 'password': 'hash3'},
        {'username': 'bob_johnson', 'email': 'bob@example.com', 'password': 'hash4', 'role': 'admin'}
    ]
        
    for user in users_data:
        response = requests.post(f'{BASE_URL}/auth/register', json=user)
        print(response.json())

def generate_categories():
    categories_data = [
        {'name': 'Electronics'},
        {'name': 'Clothing'},
        {'name': 'Books'},
        {'name': 'Home & Kitchen'},
        {'name': 'Sports & Outdoors'}
    ]
        
    for category in categories_data:
        response = requests.post(f'{BASE_URL}/categories', json=category)
        print(response.json())

def generate_products():
    products_data = [
        {'name': 'Laptop', 'category_id': 1, 'price': 1200.99},
        {'name': 'Smartphone', 'category_id': 1, 'price': 799.99},
        {'name': 'T-shirt', 'category_id': 2, 'price': 19.99},
        {'name': 'Sneakers', 'category_id': 2, 'price': 59.99},
        {'name': 'Science Fiction Book', 'category_id': 3, 'price': 15.99},
        {'name': 'Cooking Utensils Set', 'category_id': 4, 'price': 49.99},
        {'name': 'Yoga Mat', 'category_id': 5, 'price': 29.99}
    ]
        
    for product in products_data:
        response = requests.post(f'{BASE_URL}/products', json=product)
        print(response.json())

def generate_carts():
    carts_data = [
        {'session id': 'session 1', 'items': [{'product_id': 1, 'quantity': 1}, {'product_id': 3, 'quantity': 2}]},
        {'session id': 'session 2', 'items': [{'product_id': 2, 'quantity': 1}, {'product_id': 4, 'quantity': 1}]},
        {'session id': 'session 3', 'items': [{'product_id': 1, 'quantity': 1}, {'product_id': 5, 'quantity': 1}]},
        {'session id': 'session 4', 'items': [{'product_id': 3, 'quantity': 1}, {'product_id': 6, 'quantity': 1}]},
        {'session id': 'session 5', 'items': [{'product_id': 2, 'quantity': 1}, {'product_id': 7, 'quantity': 1}]}
    ]

    for cart in carts_data:
        response = requests.post(f'{BASE_URL}/cart', json=cart)
        print(response.json())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate dummy data')
    parser.add_argument('--bypass-role', action='store_true', help='Bypass user role requirements')
    args = parser.parse_args()

    if args.bypass_role:
        set_bypass_flag() # Set the bypass flag
        # Generate dummy data
        generate_users()
        generate_categories()
        generate_products()
        generate_carts()
        clear_bypass_flag() # Clear the bypass flag
        print("Dummy data generated successfully.")
        print("Bypass flag cleared.")
    else:
        print("Please use the --bypass-role flag to generate dummy data.")
