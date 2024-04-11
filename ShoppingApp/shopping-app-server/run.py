from app import create_app

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    # Run the Flask app
    # You can specify additional parameters in app.run(),
    # such as host='0.0.0.0' to make the server publicly available,
    # or port=<different_port> to run on a different port.
    app.run(debug=True)  # Turn off debug mode in production
