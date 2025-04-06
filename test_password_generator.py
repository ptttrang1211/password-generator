import unittest
from unittest import TestCase
from password_generator import password_generator_auto, password_generator_custom


class TestPasswordGenerator(TestCase):
    def test_password_generator_auto_valid(self):
        pw = password_generator_auto(12)
        self.assertEqual(len(pw), 12)

    def test_password_generator_auto_invalid(self):
        with self.assertRaises(ValueError):
            password_generator_auto(5)

    def test_password_generator_custom_valid(self):
        pw = password_generator_custom(2, 5, 3)
        self.assertEqual(len(pw), 10)

    def test_password_generator_custom_invalid(self):
        with self.assertRaises(ValueError):
            password_generator_custom(1, 1, 1)


if __name__ == '__main__':
    unittest.main()
