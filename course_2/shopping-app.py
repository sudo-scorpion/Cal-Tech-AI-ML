#! /usr/bin/python3

import os
import binascii
import hashlib
from flask import Flask, request, redirect, session, jsonify

app = Flask(__name__)

app.secret_key = binascii.hexlify(os.urandom(24)).decode() 

users = {
    'user1': {
        'username': 'user1',
        'email': 'user1@example.com',
        'password': 'hashed_password_1',
    },
    'user2': {
        'username': 'user2',
        'email': 'user2@example.com',
        'password': 'hashed_password_2',
    },
}

categories = ['footwear', 'clothing', 'electronics']

cart = {
    "user1": ["x", "y", "z"],
    "user2": ["y", "f", "d"],
    "user3": ["z", "b", "t"],
}

# Function to hash a password
def hash_password(password):
    # You can use a stronger hashing algorithm like bcrypt or Argon2 for better security
    return hashlib.sha256(password.encode()).hexdigest()

# Function to validate user credentials
def validate_user(username, password):
    # Retrieve user data from the data source (e.g., database, dictionary)
    user_data = users.get(username)
    if user_data:
        # Retrieve stored hashed password
        stored_password = user_data.get('password')
        if stored_password:
            # Hash the input password
            hashed_password = hash_password(password)
            # Compare hashed passwords
            if hashed_password == stored_password:
                return True  # Passwords match, authentication successful
    return False  # User not found or incorrect password

# Check if user already exists
# Check if user already exists
def is_user_already_registered(username, email):
    user = users.get(username)
    print(user)
    if user is not None and user.get('email', '').lower() == email.lower():
        return True
    return False

# Home route
@app.route("/")
def home():
    return "<p>You are in home!</p>"

# Register route 
@app.route("/register", methods=['POST'])
def register():
    request_data = request.get_json()

    firstname = request_data.get('firstname')
    lastname  = request_data.get('lastname')
    username  = request_data.get('username')
    password  = request_data.get('password')  
    email     = request_data.get('email')

    if not is_user_already_registered(username, email):
        users[username] = {
            'firstname': firstname,
            'lastname': lastname,
            'username': username,
            'password': hash_password(password),
            'email': email
        }
        return jsonify({'message': 'User registered successfully', 'username': username}), 201
    else:
        return jsonify({'error': 'Username already exists'}), 400


# Login route
@app.route("/login", methods=['POST'])
def login():
    is_login_successful = 0
    if request.method == 'POST' and request.is_json:
        # Parse JSON data from request body
        request_data = request.get_json()
        username = request_data.get('username')
        password = request_data.get('password')

        # Print username and password
        print("Username:", username)
        print("Password:", password)

        if validate_user(username, password):
            print("Authentication successful")
            session['username'] = username
            is_login_successful = 1
            return jsonify({'message': 'Login successful', 'username': username}), 200
            # return redirect('/')
        else:
            print("Authentication failed")
            return jsonify({'error': 'Invalid username or password'}), 401
            # return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)

