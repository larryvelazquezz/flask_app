import unittest
from app import create_app


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Hello, World!'})

    # Add more integration tests as needed
    def test_non_existent_route(self):
        response = self.client.get('/non-existent')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
