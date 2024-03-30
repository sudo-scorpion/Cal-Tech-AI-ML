from typing import Dict
from flask import jsonify
from category import Category

class Product:
    products: Dict[int, str] = {}

    @staticmethod
    def add_product(request_data: dict):
        try:
            # Extract product data from request
            product_id = int(request_data.get('product_id'))
            product_name = request_data.get('product_name')
            category_id = int(request_data.get('category_id'))
            price = float(request_data.get('price'))

            # Check for missing required fields
            if not all([product_id, product_name, category_id, price]):
                raise ValueError("Missing required fields")

            # Check if category exists
            if category_id not in Category.categories:
                return jsonify({'error': 'Category does not exist'}), 404

            # Check if product already exists
            if product_id in Product.products:
                return jsonify({'error': 'Product already exists'}), 409

            # Add product to products dictionary
            Product.products[product_id] = {
                'product_name': product_name,
                'category_id': category_id,
                'price': price
            }

            # Return success message
            return jsonify({'message': 'Product added successfully', 'id': product_id, 'name': product_name}), 201

        except ValueError as ve:
            return jsonify({'error': str(ve)}), 400
        except Exception as e:
            # Log the error for debugging purposes
            print(f"An error occurred while adding product: {e}")
            return jsonify({'error': 'An error occurred while adding product'}), 500
        
    @staticmethod
    def delete_product(request_data: dict):
        try:
            product_id = int(request_data.get('product_id'))
            
            # Check if product exists
            if product_id not in Product.products:
                return jsonify({'error': 'Product not found'}), 404

            # Delete the product
            del Product.products[product_id]

            # Return success message
            return jsonify({'message': 'Product deleted successfully', 'id': product_id}), 200

        except Exception as e:
            # Log the error for debugging purposes
            print(f"An error occurred while deleting product: {e}")
            return jsonify({'error': 'An error occurred while deleting product'}), 500