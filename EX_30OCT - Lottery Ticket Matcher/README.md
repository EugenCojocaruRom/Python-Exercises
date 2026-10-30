EX\_30OCT - Lottery Ticket Matcher

A small lottery draws 6 numbers. Several friends bought tickets, and you check who won what.



Starting data:



winning\_numbers = \[7, 14, 23, 31, 42, 48]



tickets = \[

&#x20;   ("Ana",   \[3, 14, 23, 29, 42, 50]),

&#x20;   ("Mihai", \[7, 14, 23, 31, 42, 48]),

&#x20;   ("Elena", \[1, 2, 3, 4, 5, 6]),

&#x20;   ("Radu",  \[7, 14, 20, 31, 40, 48]),

&#x20;   ("Ioana", \[7, 14, 23, 31, 10, 11]),

]



Part 1: Show the tickets

&#x20;- Use enumerate() with start=1 to print each ticket as a numbered line, for example:

&#x09;1. Ana: 3, 14, 23, 29, 42, 50

(Hint: ", ".join(...) needs strings, so convert the numbers first.)



Part 2: Count the matches

&#x20;- For each ticket, use a list comprehension to build the list of numbers that are also in winning\_numbers. Print the matched numbers and how many there are, for example:

&#x09;Ana: 3 matches -> \[14, 23, 42]



Part 3: Prizes

&#x20;- Use if/elif/else to decide the prize from the number of matches:

&#x09;6 matches: “JACKPOT!”

&#x09;5 matches: “Big prize”

&#x09;4 matches: “Small prize”

&#x09;3 matches: “Free ticket”

&#x09;fewer than 3: “No prize”



&#x20;- Print the prize at the end of each ticket’s line.



Part 4: Summary

&#x20;- How many people won something (3 or more matches)? Print it with correct singular/plural: “1 winner” vs. “2 winners”.

&#x20;- Who had the most matches? Use max() with a lambda. (Think about what you would do if two people tied.)



Bonus (optional)

&#x20;- Ask the user to type the 6 winning numbers (with while True + try/except validation: exactly 6 numbers, each between 1 and 50, no duplicates).

&#x20;- Print the numbers nobody picked from the winning numbers (the “unlucky winners”), using a list comprehension.

