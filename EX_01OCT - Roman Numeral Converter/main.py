#Print header and separator
print("<-- Roman Numeral Converter -->")
print("-------------------------------")

#Create dictionary (as a constant) with the set of values, mapping each Roman symbol to its number
VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

#Create list of values as tuples, ordered from largest to smallest
TABLE = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]

#Define function for converting roman numerals to integers, where 's' is the Roman numeral
def roman_to_int(s):
    #Set condition for length of string (Roman numeral) = 0
    if len(s) == 0:
        return None
    #Declare variable for storing the sum and initialize it to value 0
    total = 0
    #Loop over the string
    for i, ch in enumerate(s):
        #Set condition for character not found in the string (i.e. Roman numeral)
        if ch not in VALUES:
            #Stop and return 'none' (for invalid input)
            return None
        #Set condition for checking that the next character exists and whether the current symbol is smaller than the next one
        if i + 1 < len(s) and VALUES[ch] < VALUES.get(s[i + 1], 0):
            #Subtract the value of the character from the sum
            total -= VALUES[ch]
        else:
            #Add the value of the character to the sum
            total += VALUES[ch]
    if int_to_roman(total) != s:
        return None
    #Return the value of the sum
    return total

#Define function for converting integers to roman numerals, where 'n' is the integer
def int_to_roman(n):
    #Declare variable to store the Roman numeral and initialize it as an empty string
    result = ""
    #Loop over the TABLE list from largest to smallest
    for value, symbol in TABLE:
        #Loop to check that the number is >= the value from the list
        while n >= value:
            #Add the symbol to the result string
            result += symbol
            #Subtract the value from the integer
            n -= value
    #Return the resulting string (Roman numeral)
    return result

#Test - round-trip check on every number from 1 to 3999
failures = [n for n in range(1, 4000) if roman_to_int(int_to_roman(n)) != n]
print("Failures:", failures)

#Year table
years = [1969, 1989, 2000, 2024, 3999]
for year in years:
    print(f"{year} -> {int_to_roman(year)}")

#Bonus 1: invalid input
for text in ["", "MCMXCIV", "MCMA", "IIII", "VX", "IC"]:
    result = roman_to_int(text)
    if result is None:
        print(f"'{text}': Incorrect Roman numeral")
    else:
        print(f"{text}: {result}")

#Bonus 2: longest numeral
longest = 1
longest_len = 1
for n in range(1, 4000):
    length = len(int_to_roman(n))
    if length > longest_len:
        longest = n
        longest_len = length
print(longest, int_to_roman(longest))