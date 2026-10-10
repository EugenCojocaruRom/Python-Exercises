EX\_10OCT - Bookshelf Titles Report

Scenario: You’re organizing a small home library. You have a list of books, each stored as a tuple: (title, author, pages).

e.g. books = \[

&#x20;   ("Dune", "Frank Herbert", 612),

&#x20;   ("Emma", "Jane Austen", 474),

&#x20;   ("The Hobbit", "J.R.R. Tolkien", 310),

&#x20;   ("Persuasion", "Jane Austen", 249),

&#x20;   ("Neuromancer", "William Gibson", 271),

&#x20;   ("Children of Dune", "Frank Herbert", 444),

&#x20;   ("Sense and Sensibility", "Jane Austen", 352),

]



Tasks:

&#x20;- Numbered list: Use enumerate() (starting at 1) to print every book like this:

1\. Dune by Frank Herbert (612 pages)

&#x20;- Thick books: Using a list comprehension, build a list of titles of all books with more than 400 pages, and print it.

&#x20;- Pages per author: Build a dictionary where each key is an author and each value is the total pages written by that author (in this list). Print it.

&#x20;- Longest and shortest: Find and print the title of the longest book and the shortest book (without using max() or min(), use a loop and if statements).

&#x20;- Reading time: Assuming you read 40 pages per hour, print the total hours needed to read the whole shelf, rounded to 1 decimal place.



Expected output (example for tasks 2 and 3)

&#x09;Thick books: \['Dune', 'Emma', 'Children of Dune']

&#x09;Pages per author: {'Frank Herbert': 1056, 'Jane Austen': 1075, 'J.R.R. Tolkien': 310, 'William Gibson': 271}



Bonus (optional):

&#x20;- Ask the user to type an author name with input() and print all the titles by that author. If the author isn’t found, print a friendly message.

