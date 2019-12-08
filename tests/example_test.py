import unittest
from chalicelib.example import simple_method


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(simple_method(1), 2)
