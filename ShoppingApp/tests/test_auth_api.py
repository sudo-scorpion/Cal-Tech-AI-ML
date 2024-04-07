import unittest
from app import create_app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    def test_user_registration_success(self):
        with self.app.test_client() as client:
            response = client.post('/auth/register', json={
                'username': 'testuser',
                'email': 'testuser@example.com',
                'password': 'testpassword'
            })
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['message'], 'User registered successfully.')

    def test_user_login_success(self):
        # Register a user first
        with self.app.test_client() as client:
            response = client.post('/auth/register', json={
                'username': 'testuser',
                'email': 'testuser@example.com',
                'password': 'testpassword'
            })
            self.assertEqual(response.status_code, 201)

        # Attempt to log in with the registered user credentials
        with self.app.test_client() as client:
            response = client.post('/auth/login', json={
                'username': 'testuser',
                'password': 'testpassword'
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], 'User testuser logged in successfully.')
            self.assertIsNotNone(response.json['session_id'])

if __name__ == '__main__':
    unittest.main()
