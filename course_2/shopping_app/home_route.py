from flask import Blueprint

home_route = Blueprint('home_route', __name__)

@home_route.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
    }
    .container {
        max-width: 800px;
        margin: 50px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #333;
        text-align: center;
    }
    </style>
    </head>
    <body>
    <div class="container">
        <h1>Welcome to the Demo Marketplace</h1>
    </div>
    </body>
    </html>
    """
