EX\_03OCT - Collatz Sequence Explorer

The Collatz sequence starts with any positive integer and repeats these rules until it reaches 1:



&#x20;- If the number is even, divide it by 2.

&#x20;- If the number is odd, multiply it by 3 and add 1.



&#x09;Example starting from 6: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1



Part 1: Build the sequence

Write a function collatz(n) that returns the full sequence as a list, including the starting number and the final 1.



Part 2: Print it nicely

For the starting number 27, use enumerate() to print only the first 10 steps in this format:



&#x09;Step 0: 27

&#x09;Step 1: 82

&#x09;...

&#x09;Part 3: Stats



For a starting number, print:

&#x20;- The number of steps (the sequence length minus 1)

&#x20;- The highest value the sequence reaches



Part 4: Compare many numbers (list comprehension)

Using a list comprehension, build a list of (start, steps) pairs for all starting numbers from 1 to 30. Then find and print:

&#x20;- Which starting number takes the most steps

&#x20;- How many of these numbers take fewer than 10 steps (use another list comprehension)



Bonus

&#x20;- Show the sequence for the number you found in Part 4 as a single line with arrows, e.g. 6 → 3 → 10 → ... (hint: look at " → ".join(...), and remember to convert numbers to strings).

