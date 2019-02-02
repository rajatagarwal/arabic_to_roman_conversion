import unittest
import solution

# 20 random arabic to roman converted values
correct_values = (
    (2780, 'MMDCCLXXX'),
    (1703, 'MDCCIII'),
    (14, 'XIV'),
    (3983, 'MMMCMLXXXIII'),
    (1231, 'MCCXXXI'),
    (77, 'LXXVII'),
    (2113, 'MMCXIII'),
    (2860, 'MMDCCCLX'),
    (2186, 'MMCLXXXVI'),
    (212, 'CCXII'),
    (1310, 'MCCCX'),
    (3604, 'MMMDCIV'),
    (2539, 'MMDXXXIX'),
    (3042, 'MMMXLII'),
    (3784, 'MMMDCCLXXXIV'),
    (2466, 'MMCDLXVI'),
    (701, 'DCCI'),
    (678, 'DCLXXVIII'),
    (482, 'CDLXXXII'),
    (2059, 'MMLIX')
)


class TestArabicToRomanConversion(unittest.TestCase):

    # Test Arabic to Roman logic
    def test_encode_roman_logic(self):
        for arabic, roman in correct_values:
            self.assertEqual(solution.encode_roman(arabic), roman)

    # Test Negative value as input
    def test_negative_or_zero_as_user_input(self):
        self.assertEqual(solution.user_input(-3), None)
        self.assertEqual(solution.user_input(0), None)

    # Test larger than 3,999 input
    def test_larger_than_3999_as_user_input(self):
        self.assertEqual(solution.user_input(4000), None)

    # Test random string input
    def test_string_as_user_input(self):
        self.assertEqual(solution.user_input("a"), None)

    # Test floating point input
    def test_float_as_user_input(self):
        self.assertEqual(solution.user_input(2.2), None)


if __name__ == "__main__":
    unittest.main()
