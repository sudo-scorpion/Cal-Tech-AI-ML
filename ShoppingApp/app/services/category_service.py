from app.data.data_store import categories_db
from app.models.category import Category

def add_category(name):
    category_id = len(categories_db) + 1
    new_category = Category(id=category_id, name=name)
    categories_db.append(new_category)
    return new_category

def get_all_categories():
    return categories_db

def update_category(category_id, name):
    category = next((c for c in categories_db if c.id == category_id), None)
    if category:
        category.name = name
        return category
    else:
        return None  # Implement proper error handling

def delete_category(category_id):
    global categories_db
    categories_db = [c for c in categories_db if c.id != category_id]
    return {"message": "Category deleted successfully"}
