# Arabic to Roman Conversion

### Assumptions:

1. I've considered following roman symbols and their respective values as baseline:

    * (1000, "M"),
    * (900,  "CM"),
    * (500,  "D"),
    * (400,  "CD"),
    * (100,  "C"),
    * (90,   "XC"),
    * (50,   "L"),
    * (40,   "XL"),
    * (10,   "X"),
    * (9,    "IX"),
    * (5,    "V"),
    * (4,    "IV"),
    * (1,    "I")

2. I've assumed the user input from 1 to 3999, as mentioned on wikipedia page. If required the upper limit can be lift off (***Wikipedia Text:*** In the absence of standard symbols for 5,000 and 10,000 the pattern breaks down at this point - in modern usage M is repeated up to three times. The Romans had several ways to indicate larger numbers, but for practical purposes Roman Numerals for numbers larger than 3,999 are seldom if ever used nowadays)

3. **Special Values**: Special values like 0, fractions and decimals are ignored in conversion. The input can only be in the integer format between 1 and 3999. 


# File Structure:

Project contains 2 python files:
1. solution.py - contains logic
2. test_solution.py - contains unit test cases

# Execution Instructions:

1. **Python Version**: 3.6.4
2. **OS**: Windows 10 Pro

There are 2 easy ways to run the project using commandline. Either one of the below approach should work fine.
1. **Running "solution.py"**:
    * python solution.py - 
      It will ask you to enter any decimal number. You're expected to give between 1 to 3,999 but you're free to enter anything as it covers error handling.
2. **Running "test_solution.py"**:
   * python test_solution.py - 
        It runs 20 pre-made test cases + it will check failed input type as such negative values, 0 as input, larger than 3,999 values, floating point number and any string value as input.




