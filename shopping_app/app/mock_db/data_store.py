from app.models.user import User
from app.models.session import Session
from app.models.category import Category
from app.models.product import Product
from app.models.cart import Cart
from app.models.payment import Payment
from app.utils.helper_functions import hash_password, generate_secure_id

# In-memory "database"
users = {}
sessions = {}
categories = {}
products = {}
cart = {}
payments = {}
carts = {}

# Create dummy data for users
user = User(1, "john_doe", hash_password("password123"), "john@example.com", "user")
users[user.user_id] = user
user = User(2, "jane_smith", hash_password("password456"), "jane@example.com", "admin")
users[user.user_id] = user

# Create dummy data for sessions
# session = Session('1', 1, "2022-01-01 10:00:00", True)
# sessions[session.session_id] = session
# session = Session('2', 2, "2022-01-02 15:30:00", True)
# sessions[session.session_id] = session

# Create dummy data for categories
# categories.append(Category(1, "Electronics"))

# categories.append(Category(2, "Clothing"))
category = Category(1, "Electronics")
categories[category.category_id] = category
category = Category(2, "Clothing")
categories[category.category_id] = category

# Create dummy data for products
product = Product(1, "Laptop", 1, 1000.00)
products[product.product_id] = product
product = Product(2, "T-shirt", 2, 20.00)
products[product.product_id] = product

# Create dummy data for cart
# self.payment_id = payment_id
# self.user_id = user_id
# self.amount = amount
# self.payment_method = payment_method
# self.payment_status = payment_status

payment = Payment(1, 1, 1000.00, "Credit Card", "Paid")
payments[payment.payment_id] = payment
payment = Payment(2, 2, 20.00, "Debit Card", "Paid")
payments[payment.payment_id] = payment

# Create dummy data for cart
cart = Cart(1, 1, None, 1, 2)
carts[cart.cart_id] = cart
cart = Cart(2, 2, None, 2, 3)
carts[cart.cart_id] = cart



