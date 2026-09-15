"""Unit tests for the is_armstrong() function in armstrong.py."""

import unittest

from armstrong import is_armstrong


class TestIsArmstrong(unittest.TestCase):

    def test_single_digit_numbers_are_armstrong(self):
        # Any single digit is trivially an Armstrong number (n^1 == n)
        for n in range(0, 10):
            self.assertTrue(is_armstrong(n))

    def test_known_armstrong_numbers(self):
        for n in (153, 370, 371, 407, 1634, 8208, 9474):
            self.assertTrue(is_armstrong(n))

    def test_known_non_armstrong_numbers(self):
        for n in (10, 100, 123, 200, 999, 1000):
            self.assertFalse(is_armstrong(n))

    def test_returns_a_boolean(self):
        self.assertIsInstance(is_armstrong(153), bool)
        self.assertIsInstance(is_armstrong(100), bool)


if __name__ == "__main__":
    unittest.main()
