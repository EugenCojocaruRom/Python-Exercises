EX\_02OCT - Twin Prime Finder

Goal: Find all pairs of "twin primes" up to a given limit. Twin primes are two primes that differ by exactly 2, like (3, 5) or (11, 13).



Instructions

&#x20;- Ask the user for a limit (for example, 50).

&#x20;- Write a function is\_prime(n) that returns True if n is prime and False otherwise.

&#x09; -> Numbers below 2 are not prime.

&#x09; -> Check divisors from 2 up to the square root of n (int(n \*\* 0.5) + 1).

&#x20;- Use a list comprehension to build a list of all primes from 2 up to the limit.

&#x20;- Loop through that list with enumerate() and compare each prime to the next one. If the difference is 2, store the pair as a tuple.

&#x20;- Print each pair on its own line, numbered, then print a summary.



Hints

&#x20;- For step 4, enumerate(primes) gives you the index i, so you can look at primes\[i + 1]. Be careful not to go past the end of the list!

&#x20;- If no pairs exist (for example, with a limit of 4), print a friendly message instead of an empty list.



Bonus (optional)

&#x20;- Also find prime triplets, like (3, 5, 7), where three primes fit within a span of 6.

&#x20;- Handle invalid input (negative numbers or text) without crashing, using try/except.

