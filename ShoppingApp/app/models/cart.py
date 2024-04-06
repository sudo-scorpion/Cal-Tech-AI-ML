class CartItem:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

class Cart:
    def __init__(self, session_id, items=None):
        self.session_id = session_id
        self.items = items if items is not None else []

    def get_items(self):
        return self.items
