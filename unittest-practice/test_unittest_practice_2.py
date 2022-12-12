import unittest
from tested_functions import divider


class TestDivider(unittest.TestCase):
    """Requirements to test:

    - Returns non-integer results (does not floor divide)
    - Raises ValueError if too many or too few arguments provided (division is binary)
    - Raises TypeError if non-integer arguments provided
    - Raises ValueError if attempting to divide by 0 (treating the error as a bad argument issue, not a math issue)
    - Handles arbitrarily large integer dividends/divisors
    - Can be called multiple times in succession accurately (divider(divider(divider(...
    """

    def test_divides_two_integers_correctly(self):
        self.assertEqual(divider(10, 2), 5)

    def test_returns_non_integer_results(self):
        self.assertEqual(divider(10, 5), 2.0)

    def test_raises_type_error_with_non_integer_args(self):
        self.assertRaises(TypeError, divider, 10.0, 2)

    def test_raises_value_error_with_other_than_two_args(self):
        self.assertRaises(ValueError, divider, 10, 2, 5)
        self.assertRaises(ValueError, divider, 10)

    def test_raises_type_error_when_divided_by_zero(self):
        self.assertRaises(ValueError, divider, 10, 0)

    def test_works_with_large_integers(self):
        self.assertEqual(divider(10**1000, 10**999), 10)

    def test_works_in_a_nested_fashion(self):
        # does not work because divider accepts integers but returns float
        self.assertEqual(divider(divider(100, 2), divider(100, 4)), 2)
