class Cart:
    def __init__(self, cart_id, user_id, session_id, product_id, quantity):
        self.cart_id = cart_id
        self.user_id = user_id
        self.session_id = session_id
        self.product_id = product_id
        self.quantity = quantity

    def __json__(self):
        return {
            "cart_id": self.cart_id,
            "user_id": self.user_id,
            "session_id": self.session_id,
            "product_id": self.product_id,
            "quantity": self.quantity
        }