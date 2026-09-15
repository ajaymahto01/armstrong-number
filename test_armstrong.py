"""Unit tests for the Armstrong number functions in armstrong.py."""

import unittest

from armstrong import is_armstrong, is_armstrong_recursive

ARMSTRONG_FUNCTIONS = (is_armstrong, is_armstrong_recursive)


class TestIsArmstrong(unittest.TestCase):

    def test_single_digit_numbers_are_armstrong(self):
        # Any single digit is trivially an Armstrong number (n^1 == n)
        for func in ARMSTRONG_FUNCTIONS:
            for n in range(0, 10):
                self.assertTrue(func(n))

    def test_known_armstrong_numbers(self):
        for func in ARMSTRONG_FUNCTIONS:
            for n in (153, 370, 371, 407, 1634, 8208, 9474):
                self.assertTrue(func(n))

    def test_known_non_armstrong_numbers(self):
        for func in ARMSTRONG_FUNCTIONS:
            for n in (10, 100, 123, 200, 999, 1000):
                self.assertFalse(func(n))

    def test_returns_a_boolean(self):
        for func in ARMSTRONG_FUNCTIONS:
            self.assertIsInstance(func(153), bool)
            self.assertIsInstance(func(100), bool)

    def test_loop_and_recursive_versions_agree(self):
        for n in range(0, 1001):
            self.assertEqual(is_armstrong(n), is_armstrong_recursive(n))


if __name__ == "__main__":
    unittest.main()
