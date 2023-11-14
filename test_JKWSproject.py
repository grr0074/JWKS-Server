import unittest
from JKWSproject import app

class TestJKWSProject(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_jwks_endpoint(self):
        response = self.app.get('/jwks')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('keys', data)

    def test_auth_endpoint(self):
        response = self.app.post('/auth')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('token', data)

    def test_auth_endpoint_expired(self):
        response = self.app.post('/auth?expired=true')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('token', data)

if __name__ == '__main__':
    unittest.main()
