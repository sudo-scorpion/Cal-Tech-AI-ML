from flask_restx import Namespace, Resource, fields
from app.services.auth_service import add_user, authenticate_user, get_all_users

# Define the namespace
auth_ns = Namespace('auth', description='Authentication related operations.')

# Request model for user registration
registration_model = auth_ns.model('Registration', {
    'username': fields.String(required=True, description='Username'),
    'email': fields.String(required=True, description='Email address'),
    'password': fields.String(required=True, description='Password'),
})

# Request model for user login
login_model = auth_ns.model('Login', {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password'),
})

# Registration route
@auth_ns.route('/register')
class UserRegister(Resource):
    @auth_ns.expect(registration_model)
    def post(self):
        """Register a new user."""
        data = auth_ns.payload
        if add_user(data['username'], data['email'], data['password']):
            return {'message': 'User registered successfully.'}, 201
        else:
            return {'message': 'Registration failed.'}, 400

# Login route
@auth_ns.route('/login')
class UserLogin(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        """Log in a user."""
        data = auth_ns.payload
        user = authenticate_user(data['username'], data['password'])
        if user:
            # For simplicity, returning a mock session ID. Implement actual session management.
            return {'message': f'User {user.username} logged in successfully.', 'session_id': 'mock_session_id'}, 200
        else:
            return {'message': 'Username or password is incorrect.'}, 401
        
# Logout route
@auth_ns.route('/logout')
class UserLogout(Resource):
    def post(self):
        """Log out a user."""
        # For simplicity, returning a mock message. Implement actual session management.
        return {'message': 'User logged out successfully.'}, 200
    
# Get all users route
@auth_ns.route('/users')
class AllUsers(Resource):
    @auth_ns.marshal_list_with(registration_model)
    def get(self):
        """Get all users."""
        return get_all_users(), 200


