import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app"))
)

from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"DevOps Support Service", response.data)
        self.assertIn(b"1.0.0", response.data)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")
        self.assertEqual(response.json["version"], "1.0.0")

    def test_not_found(self):
        response = self.client.get("/missing")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
