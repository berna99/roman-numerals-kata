import unittest
from roman_numerals import to_roman

class TestRomanNumerals(unittest.TestCase):

    def test_basic_numerals(self):
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(5), 'V')
        self.assertEqual(to_roman(10), 'X')
        self.assertEqual(to_roman(50), 'L')
        self.assertEqual(to_roman(100), 'C')
        self.assertEqual(to_roman(500), 'D')
        self.assertEqual(to_roman(1000), 'M')

    def test_combinations(self):
        self.assertEqual(to_roman(2), 'II')
        self.assertEqual(to_roman(3), 'III')
        self.assertEqual(to_roman(6), 'VI')
        self.assertEqual(to_roman(7), 'VII')
        self.assertEqual(to_roman(8), 'VIII')
        self.assertEqual(to_roman(11), 'XI')
        self.assertEqual(to_roman(15), 'XV')
        self.assertEqual(to_roman(20), 'XX')
        self.assertEqual(to_roman(30), 'XXX')
        self.assertEqual(to_roman(60), 'LX')
        self.assertEqual(to_roman(70), 'LXX')
        self.assertEqual(to_roman(80), 'LXXX')
        self.assertEqual(to_roman(110), 'CX')
        self.assertEqual(to_roman(150), 'CL')
        self.assertEqual(to_roman(200), 'CC')
        self.assertEqual(to_roman(300), 'CCC')
        self.assertEqual(to_roman(600), 'DC')
        self.assertEqual(to_roman(700), 'DCC')
        self.assertEqual(to_roman(800), 'DCCC')
        self.assertEqual(to_roman(1100), 'MC')
        self.assertEqual(to_roman(1500), 'MD')
        self.assertEqual(to_roman(2000), 'MM')
        self.assertEqual(to_roman(3000), 'MMM')

    def test_subtraction_rule(self):
        self.assertEqual(to_roman(4), 'IV')
        self.assertEqual(to_roman(9), 'IX')
        self.assertEqual(to_roman(40), 'XL')
        self.assertEqual(to_roman(90), 'XC')
        self.assertEqual(to_roman(400), 'CD')
        self.assertEqual(to_roman(900), 'CM')

    def test_complex_numbers(self):
        self.assertEqual(to_roman(1994), 'MCMXCIV')
        self.assertEqual(to_roman(2024), 'MMXXIV')
        self.assertEqual(to_roman(3999), 'MMMCMXCIX')

    def test_edge_cases(self):
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(3999), 'MMMCMXCIX')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            to_roman(0)
        with self.assertRaises(ValueError):
            to_roman(4000)
        with self.assertRaises(ValueError):
            to_roman(-1)

if __name__ == '__main__':
    unittest.main()


