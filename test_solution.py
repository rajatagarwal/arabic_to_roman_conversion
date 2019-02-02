import unittest
import solution

# 20 random arabic to roman converted true values 
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


	def test_encode_roman_logic(self):
		# Matches Roman value from the function with known Roman values for the Arabic Numbers
		for arabic, roman in correct_values:
			self.assertEqual(solution.encode_roman(arabic), roman)

	
	def test_negative_or_zero_input(self):
		# Returns None with anything smaller than 1
		self.assertEqual(solution.user_input(-3), None)


	def test_larger_than_3999_input(self):
		# Returns None with anything larger than 3999
		self.assertEqual(solution.user_input(4000), None)


	def test_garbage_user_input(self):
		# Returns None for string input
		self.assertEqual(solution.user_input("a"), None)


	def test_float_input(self):
		# Returns None for float input
		self.assertEqual(solution.user_input(2.2), None)


if __name__ == "__main__":
	unittest.main()