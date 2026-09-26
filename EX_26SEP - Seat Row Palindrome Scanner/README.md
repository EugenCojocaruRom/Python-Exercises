EX\_26SEP - Seat Row Palindrome Scanner

A theater has rows of seat labels stored as strings, like "A1B2C1A". A row is considered "balanced" if the letters only (ignoring numbers) read the same forwards and backwards.



Your task:



&#x20;- Write a function extract\_letters(seat\_code) that returns just the letters from a seat code, in order (use a list comprehension, e.g. filter with .isalpha()).

&#x20;- Write a function is\_balanced(seat\_code) that returns True if the extracted letters form a palindrome, False otherwise.

&#x20;- Given this list of seat codes:

&#x09;seat\_codes = \["A1B2B1A", "X9Y8Z7", "M3O2M1", "R1A2C1E", "L1E2V1E1L"]



&#x20;- Use enumerate() to print each seat code's row number (starting at 1) alongside whether it's balanced, like:



&#x20;  Row 1: A1B2B1A -> Balanced

&#x20;  Row 2: X9Y8Z7 -> Not balanced

&#x20;  ...



Bonus: at the end, print how many rows out of the total are balanced, using a list comprehension to count them.

