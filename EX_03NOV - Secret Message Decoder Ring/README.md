EX\_03NOV - Secret Message Decoder Ring

Goal: Convert a word or sentence into the position of each letter in the alphabet (A=1, B=2, ... Z=26), and then convert numbers back into letters.



Part 1: Encode



Write a function encode(text) that:

&#x20;- Takes a string like "Hello World".

&#x20;- Ignores spaces and punctuation, and treats upper and lower case the same.

&#x20;- Returns a list of numbers, e.g. \[8, 5, 12, 12, 15, 23, 15, 18, 12, 4].



Hint: string.ascii\_lowercase gives you "abcdefghijklmnopqrstuvwxyz", and you can use enumerate(..., start=1) to build a dictionary of letter → position.



Part 2: Decode



Write a function decode(numbers) that takes a list of numbers and returns the string, e.g. \[8, 9] → "hi".



Part 3: Report



Using a list comprehension, print:

&#x20;- The encoded numbers for the sentence "Python is fun".

&#x20;- The sum of all the numbers.

&#x20;- The letter with the highest value (the letter furthest along in the alphabet) in the sentence.

&#x20;- Whether decoding the encoded list gives back the original letters (without spaces).



Example output

Encoded: \[16, 25, 20, 8, 15, 14, 9, 19, 6, 21, 14]

Sum: 167

Highest letter: y (25)

Round trip OK: True



Bonus (optional):

&#x20;- Add a shift parameter to encode, so that encode("abc", shift=1) returns \[2, 3, 4]. Make it wrap around, so z shifted by 1 becomes 1 again.

