import os
import binascii
from flask import Flask
from home_route import home_route
from user_routes import user_routes
from category_routes import category_routes
from product_routes import product_routes

app = Flask(__name__)
app.secret_key = binascii.hexlify(os.urandom(24)).decode() 

# Register the home route blueprint
app.register_blueprint(home_route)

# Register the user routes blueprint
app.register_blueprint(user_routes)

# Register the category routes blueprint
app.register_blueprint(category_routes)

# Register the product routes blueprint
app.register_blueprint(product_routes)


if __name__ == '__main__':
    app.run(debug=True)