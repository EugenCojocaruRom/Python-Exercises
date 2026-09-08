EX\_08SEP - Neighborhood Book Swap Tracker

You're helping run a local book swap. For each book dropped off, collect: donor name, book title, and condition (New / Good / Worn).



Core tasks:

&#x20;- Ask the user how many books are being dropped off (validate it's a positive integer).

&#x20;- For each book, collect donor name, title, and condition (validate condition is one of the three allowed values — case-insensitive is a nice touch but not required).

&#x20;- Store each entry as a tuple: (donor, title, condition).

&#x20;- Print a numbered list of all donations using enumerate() (start at 1).

&#x20;- Use a list comprehension to build a list of just the "New" condition books, and print how many there are (handle singular/plural: "1 new book" vs "3 new books" vs "0 new books").

&#x20;- Print the total number of books donated.



Bonus (optional):

&#x20;- Use a dictionary to count how many books each donor contributed, then print a leaderboard sorted by donation count, descending.

&#x20;- Add a second list comprehension that finds all book titles containing a word the user searches for (case-insensitive).

