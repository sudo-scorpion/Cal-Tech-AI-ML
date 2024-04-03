from app.models.product import Product
from app.mock_db.data_store import products
from flask import jsonify

# Product services
def create_product(product_name, category_id, price):
    try:
        product_id = products.__sizeof__() + 1
        product = Product(product_id, product_name, category_id, price)
        products[product_id] = product
        return jsonify({'message': 'Product created successfully', 'product': product.__json__()}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})

def get_product(product_id):
    try:
        product = products.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        return jsonify({'product': product.__json__()}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})

def get_all_products():
    try:
        return jsonify({'products': [product.__json__() for product in products.values()]}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})

def update_product(product_id, product_name=None, category_id=None, price=None):
    try:
        product = products.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        if product_name:
            product.product_name = product_name
        if category_id:
            product.category_id = category_id
        if price:
            product.price = price
        products[product_id] = product
        return jsonify({'message': 'Product updated successfully', 'product': product.__json__()}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})

def delete_product(product_id):
    try:
        product = products.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        del products[product_id]
        return jsonify({'message': 'Product deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request', 'message': str(e)})
