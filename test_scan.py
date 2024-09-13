# test_scan.py
import unittest
from scan import scan_web_app

class TestScan(unittest.TestCase):
    def test_scan(self):
        # Replace with actual test logic
        result = scan_web_app("https://juice-shop.herokuapp.com/#/login")
        self.assertIn("Forms:", result)
        self.assertIn("Input Fields:", result)

if __name__ == "__main__":
    unittest.main()
