class CartItem:
    def __init__(self, product_id: int, quantity: int):
        self.product_id = product_id
        self.quantity = quantity
class Cart:
    def __init__(self, session_id, items=None):
        self.session_id = session_id
        self.items = items if items is not None else []

    def get_items(self):
        return self.items
    
    def add_item(self, product_id: int, quantity: int):
        existing_item = next((item for item in self.items if int(item.product_id) == int(product_id)), None)
        if existing_item:
            existing_item.quantity += quantity
        else:
            self.items.append(CartItem(product_id, quantity))
    
    def remove_item(self, product_id: int):
        self.items = [item for item in self.items if int(item.product_id) != int(product_id)]

    def update_quantity(self, product_id: int, quantity: int):
        item = next((item for item in self.items if int(item.product_id) == int(product_id)), None)
        if item:
            item.quantity = quantity
        else:
            self.add_item(product_id, quantity)
    
    def clear(self):
        self.items.clear()

# Path: ShoppingApp/app/data/data_store.py

    

