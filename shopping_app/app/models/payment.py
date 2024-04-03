class Payment:
    def __init__(self, payment_id, user_id, amount, payment_method, payment_status):
        self.payment_id = payment_id
        self.user_id = user_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_status = payment_status

    def __json__(self):
        return {
            'payment_id': self.payment_id,
            'user_id': self.user_id,
            'amount': self.amount,
            'payment_method': self.payment_method,
            'payment_status': self.payment_status
        }
        
    def __str__(self):
        return f'Payment ID: {self.payment_id}, User ID: {self.user_id}, Amount: {self.amount}, Payment Method: {self.payment_method}, Payment Status: {self.payment_status}'
    