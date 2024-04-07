import unittest
from ShoppingApp.app import create_app

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        
    def setUp(self):
        self.client = self.app.test_client()

    @classmethod
    def tearDownClass(cls):
        # Perform any necessary cleanup
        pass

    def test_user_registration_success(self):
        response = self.client.post('/auth/register', json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201, msg="User registration failed")
        self.assertEqual(response.json['message'], 'User registered successfully.', msg="Incorrect success message")

    def test_user_login_success(self):
        # Register a user first
        self.client.post('/auth/register', json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        })

        # Attempt to log in with the registered user credentials
        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200, msg="User login failed")
        self.assertEqual(response.json['message'], 'User testuser logged in successfully.', msg="Incorrect success message")
        self.assertIsNotNone(response.json['session_id'], msg="Session ID not found")

if __name__ == '__main__':
    unittest.main()
