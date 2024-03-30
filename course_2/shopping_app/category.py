from typing import Dict
from flask import jsonify

class Category:
    categories: Dict[int, str] = {}

    # Add category 
    @staticmethod
    def add_category(request_data):
        try:
            # Extract request data
            id: int = request_data.get('id')
            name: str = request_data.get('name')

            if not all([id, name]):
                raise ValueError("Missing required fields")
            
            if id in Category.categories:
                return jsonify({'error': 'Category cannot be added, already exists', 'id': id, 'name': name}), 401
            
            Category.categories[id] = name

            return jsonify({'message': 'Category added successfully', 'id': id, 'name': name}), 201
    
        except Exception as e:
            return jsonify({'error': 'An error occurred while adding category'}), 500

    # Delete category 
    @staticmethod
    def delete_category(request_data):
        try:
            # Extract request data
            id: int = request_data.get('id')

            if not id:
                raise ValueError("Missing required fields")
            
            if id not in Category.categories:
                return jsonify({f"id:{id} doesn't exist"}), 400 
            
            del Category.categories[id]

            return jsonify({'message': 'Category deleted successfully', 'id': id}), 201
    
        except Exception as e:
            return jsonify({'error': 'An error occurred while adding category'}), 500