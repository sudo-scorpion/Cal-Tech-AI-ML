# Flask Shopping Application

This Flask shopping application provides a simple backend with RESTful APIs for managing users, products, categories, carts, and checkout processes. It includes a Swagger UI for easy testing and interaction with the APIs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- pip
- Docker

### Installing

A step-by-step series of examples that tell you how to get a development environment running.

1. **Clone the repository**

    ```bash
    git clone https://github.com/sudo-scorpion/Cal-Tech-AI-ML.git
    cd ShoppingApp
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python run.py
    ```

    This command starts the Flask development server. By default, the application will be accessible at http://127.0.0.1:5000/.

### Using Docker

Alternatively, you can run the application using Docker. Follow these steps:

1. Pull the Docker image from Docker Hub:

    ```bash
    docker pull sudo-scorpion/shopping-app
    ```

2. Run the Docker container:

    ```bash
    docker run -p 5000:5000 sudo-scorpion/shopping-app
    ```

    This command starts the Flask application inside a Docker container. By default, the application will be accessible at http://127.0.0.1:5000/.

### Using the Swagger UI

The Flask application is configured with Flask-RESTx, which automatically generates a Swagger UI for the application's API.

Access the Swagger UI: Open a web browser and navigate to http://127.0.0.1:5000/. You'll be presented with the Swagger UI, listing all available API endpoints.

Test the APIs:
- You can expand each API endpoint to see its documentation, required parameters, and the model it expects.
- To test an endpoint, click on the "Try it out" button, fill in the required parameters, and then click "Execute".
- The Swagger UI will display the request as it was sent, the server's response, and the response body.

### Key Endpoints

User Registration and Login:
- `/auth/register` - Register a new user.
- `/auth/login` - Login as an existing user.

Product Management:
- `/products/` - List all products or add a new product.
- `/products/{id}` - Retrieve, update, or delete a specific product.

Category Management:
- `/categories/` - List all categories or add a new category.
- `/categories/{id}` - Retrieve, update, or delete a specific category.

Cart Operations:
- `/cart/` - View the cart or add items to the cart.
- `/cart/{product_id}` - Remove or update quantity of a specific item in the cart.

Checkout:
- `/checkout/` - Process the checkout of the current cart.

### Development Notes

- This application uses an in-memory data store for demonstration purposes. For production use, consider integrating a persistent database.
- Passwords are stored as plain text in this example. In a real application, ensure passwords are hashed before storage.

### Contributing

Feel free to fork the repository and submit pull requests.

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.