
# Format: (base_arabic, base_roman)
base_conversions = [
	(1000, "M"),
	(900,  "CM"),
	(500,  "D"),
	(400,  "CD"),
	(100,  "C"),
	(90,   "XC"),
	(50,   "L"),
	(40,   "XL"),
	(10,   "X"),
	(9,    "IX"),
	(5,    "V"),
	(4,    "IV"),
	(1,    "I")
]


def encode_roman(arabic_number):
	roman_value = ""

	while arabic_number > 0:
		for base_arabic, base_roman  in base_conversions:
			while arabic_number >= base_arabic:
				roman_value += base_roman
				arabic_number -= base_arabic
	return roman_value


def user_input(user_input):
	try:
		if isinstance(user_input, float):
			raise ValueError
		
		arabic_number = int(user_input)

		if 0 < arabic_number < 4000:
			return arabic_number
		else:
			print("Please enter a integer within 1 to 3999.")
	
	except ValueError:
		print("Please enter integers only")


if __name__ == "__main__":
	arabic_number = user_input(input("Enter an arabic number:"))
	if arabic_number is not None:
		print(encode_roman(arabic_number))
