import unittest
from flask_app.app import app

class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        # Send a GET request to the root URL
        response = self.app.get("/")
        
        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the response data matches "Hello, World!"
        self.assertEqual(response.data.decode('utf-8'), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
