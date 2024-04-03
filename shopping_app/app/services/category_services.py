from app.models.category import Category
from app.mock_db.data_store import categories
from flask import jsonify

# Category services
def create_category(category_name: str):
    try:
        category_id = len(categories) + 1
        category = Category(category_id, category_name)
        categories[category_id] = category
        return jsonify({'message': 'Category created successfully', 'category': category.__json__()}), 201
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    
def get_category(category_id):
    try:
        category = categories.get(category_id)
        if category:
            return jsonify(category.__json__()), 200
        else:
            return jsonify({'error': 'Category not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
def get_all_categories():
    try:
        return jsonify([category.__json__() for category in categories.values()]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def update_category(category_id, category_name=None):
    try: 
        category = categories.get(category_id)
        if category:
            category.category_name = category_name
            return jsonify({'message': 'Category updated successfully', 'category': category.__json__()}), 200
        else:
            return jsonify({'error': 'Category not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def delete_category(category_id):
    try:
        category = categories.pop(category_id, None)
        if category:
            return jsonify({'message': 'Category deleted successfully'}), 200
        else:
            return jsonify({'error': 'Category not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500