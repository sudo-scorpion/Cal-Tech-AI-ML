from flask import Flask
from flask_restx import Api
from app.api.namespaces.auth_ns import auth_ns
from app.api.namespaces.category_ns import category_ns
from app.api.namespaces.product_ns import product_ns
from app.api.namespaces.cart_ns import cart_ns
from app.api.namespaces.checkout_ns import checkout_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, title='Shopping App', version='1.0', description='A simple shopping API')
    
    # Register namespaces
    api.add_namespace(auth_ns, path='/auth')
    api.add_namespace(category_ns, path='/categories')
    api.add_namespace(product_ns, path='/products')
    api.add_namespace(cart_ns, path='/cart')
    api.add_namespace(checkout_ns, path='/checkout')
    return app
