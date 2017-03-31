import unittest

class MainTestCase(unittest.TestCase):
    def test_adding_two_numbers(self):
        self.assertEqual(2 + 3, 5)
