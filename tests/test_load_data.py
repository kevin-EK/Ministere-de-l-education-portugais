import unittest
from app import load_data

class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        data = load_data()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()