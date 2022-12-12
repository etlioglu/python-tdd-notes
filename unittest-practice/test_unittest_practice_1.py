import unittest
from tested_functions import adder


class TestAdder(unittest.TestCase):
    def test_adds_two_integers_correctly(self):
        self.assertEqual(adder(3, 5), 8)

    def test_adds_negative_numbers_correctly(self):
        self.assertEqual(adder(-3, -5), -8)

    def test_adds_numbers_to_zero_correctly(self):
        self.assertEqual(adder(3, 0), 3)

    def test_adds_three_integers_correctly(self):
        self.assertEqual(adder(3, 5, 8), 16)

    def test_adds_forty_integers_correctly(self):
        self.assertEqual(
            adder(
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38,
                39,
                40,
            ),
            820,
        )

    def test_raises_an_exception_when_given_one_argument(self):
        self.assertRaises(ValueError, adder, 3)

    def test_raises_an_exception_on_string_arguments(self):
        self.assertRaises(TypeError, adder, "3", "3")
