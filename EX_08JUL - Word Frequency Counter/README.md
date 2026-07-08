EX\_08JUL - Word Frequency Counter

Take a sentence (or paragraph) from the user and find out how many times each word appears, then show the results sorted from most to least frequent.



Requirements:

&#x20;- Ask the user to input a sentence.

&#x20;- Normalize it a bit (lowercase, strip punctuation — keep it simple, maybe just handle periods/commas).

&#x20;- Split it into words and count how often each one appears.

&#x20;- Print the results sorted by frequency (highest first), using enumerate() to number the output lines like:



&#x20;  1. the — 3 times

&#x20;  2. fox — 2 times

&#x20;  3. quick — 1 time



Bonus (optional): ignore common "stop words" like "the", "a", "is" using a list comprehension to filter them out before counting.

