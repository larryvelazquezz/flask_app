import unittest
from app import create_app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Hello, World!'})


if __name__ == '__main__':
    unittest.main()
