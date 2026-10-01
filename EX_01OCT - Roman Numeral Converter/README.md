EX\_01OCT - Roman Numeral Converter

Part 1: Roman numeral to integer

Write a function roman\_to\_int(s) that converts a Roman numeral string to an integer.



Use this lookup:



&#x09;values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}



The rule: normally you add the values left to right. But if a symbol is smaller than the one right after it, you subtract it instead.



&#x09;"VIII" → 5 + 1 + 1 + 1 = 8

&#x09;"IX" → I is smaller than X, so −1 + 10 = 9

&#x09;"MCMXCIV" → 1000 + (−100 + 1000) + (−10 + 100) + (−1 + 5) = 1994



Hint: use enumerate() to loop over the string with its index, so you can peek at the next character with s\[i + 1] (be careful at the last character!).



Part 2: Integer to Roman numeral

Write a function int\_to\_roman(n) that converts an integer from 1 to 3999 to a Roman numeral.



Use this table, ordered from largest to smallest:



&#x09;table = \[

&#x20;   	(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),

&#x20;   	(100, "C"), (90, "XC"), (50, "L"), (40, "XL"),

&#x20;   	(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),

&#x09;]



Idea: go through the table, and for each pair, keep subtracting the value from n (and adding the symbol to your result) while n is at least that value.



&#x09;int\_to\_roman(58) → "LVIII"

&#x09;int\_to\_roman(1994) → "MCMXCIV"



Part 3: Test it

Use a list comprehension to run a round-trip check on every number from 1 to 3999:



&#x09;all(roman\_to\_int(int\_to\_roman(n)) == n for n in range(1, 4000))



Or, to practice list comprehension, build a list of the numbers that fail and print it. It should be empty.



Also print a small table for these years:



&#x09;years = \[1969, 1989, 2000, 2024, 3999]



Stretch goals (optional):

&#x20;- Make roman\_to\_int return None (or print an error) if the string contains an invalid character like "A".

&#x20;- Find which number from 1 to 3999 has the longest Roman numeral.

