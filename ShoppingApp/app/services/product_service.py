from app.data.data_store import products_db
from app.models.product import Product

def add_product(name, category_id, price):
    product_id = len(products_db) + 1
    new_product = Product(id=product_id, name=name, category_id=category_id, price=price)
    products_db.append(new_product)
    return new_product

def get_all_products():
    return products_db

def update_product(product_id, name, category_id, price):
    product = next((p for p in products_db if p.id == product_id), None)
    if product:
        product.name = name
        product.category_id = category_id
        product.price = price
        return product
    return None  # Consider implementing proper error handling here

def delete_product(product_id):
    global products_db
    products_db = [product for product in products_db if product.id != product_id]
    return {"message": "Product deleted successfully"}
