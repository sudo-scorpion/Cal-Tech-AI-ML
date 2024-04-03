class Product:
    def __init__(self, product_id, product_name, category_id, price):
        self.product_id = product_id
        self.product_name = product_name
        self.category_id = category_id
        self.price = price

    def __json__(self):
        return {'product_id': self.product_id, 'product_name': self.product_name, 'category_id': self.category_id, 'price': self.price}
    
    def __str__(self):
        return f'Product ID: {self.product_id}, Product Name: {self.product_name}, Category ID: {self.category_id}, Price: {self.price}'
    
