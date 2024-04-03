import os
import binascii
from flask import Flask
from app.routes.user_routes import user_routes
from app.routes.auth_routes import auth_routes
from app.routes.session_routes import session_routes
from app.routes.product_routes import product_routes
from app.routes.cart_routes import cart_routes
from app.routes.category_routes import category_routes
from app.routes.payment_routes import payment_routes

def create_app():
    # Create a Flask app
    app = Flask(__name__)
    # Generate a secret key for the app
    app.secret_key = binascii.hexlify(os.urandom(24)).decode() 
    # Register the blueprints with the Flask app
    app.register_blueprint(user_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(session_routes)
    app.register_blueprint(product_routes)
    app.register_blueprint(cart_routes)
    app.register_blueprint(category_routes)
    app.register_blueprint(payment_routes)
    return app
