import unittest
from main import add, subtract, multiply, divide, is_positive

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(10, -5), 15)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(4, 0.5), 2.0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(10, 4), 2.5)
        self.assertIsNone(divide(5, 0)) # Teste para divisão por zero
        self.assertEqual(divide(0, 5), 0)

    def test_is_positive(self):
        self.assertTrue(is_positive(5))
        self.assertFalse(is_positive(-1))
        self.assertFalse(is_positive(0))
        self.assertTrue(is_positive(0.001))

if __name__ == '__main__':
    unittest.main()