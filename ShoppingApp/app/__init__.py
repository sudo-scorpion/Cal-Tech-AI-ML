import os
import binascii
from flask import Flask
from flask_restx import Api
from app.api.namespaces.auth_ns import auth_ns
from app.api.namespaces.category_ns import category_ns
from app.api.namespaces.product_ns import product_ns
from app.api.namespaces.cart_ns import cart_ns
from app.api.namespaces.checkout_ns import checkout_ns

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    app.secret_key = binascii.hexlify(os.urandom(24)).decode()

    # Session cookie settings
    app.config['SESSION_COOKIE_NAME'] = 'ShoppingAppSession'
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'
    app.config['SESSION_COOKIE_MAX_AGE'] = 3600

    # Session storage settings
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_FILE_DIR'] = '/tmp'
    app.config['SESSION_FILE_THRESHOLD'] = 500
    app.config['SESSION_FILE_AGE'] = 86400
    app.config['SESSION_FILE_GC_FREQ'] = 100

    # Initialize the API
    api = Api(app, title='Shopping App', version='1.0', description='Welcome to the Demo Marketplace')
    
    # Register namespaces
    api.add_namespace(auth_ns, path='/auth')
    api.add_namespace(category_ns, path='/categories')
    api.add_namespace(product_ns, path='/products')
    api.add_namespace(cart_ns, path='/cart')
    api.add_namespace(checkout_ns, path='/checkout')
    return app
