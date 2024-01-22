import unittest
from main import main_function

class TestMain(unittest.TestCase):
    def test_output(self):
        self.assertEqual(main_function(), "Hello World")

if __name__ == '__main__':
    unittest.main()