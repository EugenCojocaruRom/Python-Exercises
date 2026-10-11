EX\_11OCT - Book Shelf Organizer (with functions)

Have a predefined list of books, each stored as a tuple: (title, author, pages).



books = \[

&#x20;   ("Dune", "Frank Herbert", 612),

&#x20;   ("Emma", "Jane Austen", 474),

&#x20;   ("The Hobbit", "J.R.R. Tolkien", 310),

&#x20;   ("Persuasion", "Jane Austen", 249),

&#x20;   ("Neuromancer", "William Gibson", 271),

&#x20;   ("Children of Dune", "Frank Herbert", 444),

&#x20;   ("Sense and Sensibility", "Jane Austen", 352),

]



Tasks:

Write these functions. Each one should return a value (not print it), and you print the results outside the functions.

&#x20;- get\_thick\_books(books, min\_pages) returns a list of titles with at least min\_pages pages.

&#x20;- pages\_per\_author(books) returns a dictionary of author → total pages.

&#x20;- find\_by\_author(books, author\_name) returns a list of titles by that author (case-insensitive).

&#x20;- sort\_books(books, by) returns a new sorted list of books. If by is "title", sort alphabetically by title. If by is "pages", sort by number of pages, from the longest to the shortest.

&#x20;- Add a text menu that uses them.

&#x09;1. Show thick books

&#x09;2. Pages per author

&#x09;3. Find books by author

&#x09;4. Sort books

&#x09;0. Quit

&#x20;- Use a while True loop that shows the menu, asks for a choice, and repeats until the user enters 0.

&#x20;- Option 1: ask for the minimum number of pages and print the result of get\_thick\_books.

&#x20;- Option 2: print the result of pages\_per\_author, one author per line (remember .items()).

&#x20;- Option 3: ask for an author name and print the titles. If the list is empty, print a friendly message.

&#x20;- Option 4: ask whether to sort by title or pages, then print the sorted books in the numbered format from your first exercise, using enumerate().

&#x20;- Invalid choice: if the user enters something that isn’t in the menu, print a message and show the menu again.



Hints:

&#x20;- sorted(books, key=lambda book: book\[2]) sorts by the third item of each tuple.

&#x20;- Add reverse=True to sort from largest to smallest.

&#x20;- A lambda is just a tiny unnamed function. lambda book: book\[2] means “given a book, return its page count”.



Bonus:

&#x20;- Make sort\_books return the original order unchanged if by is anything other than "title" or "pages".

&#x20;- Handle the case where the user types text instead of a number when asked for the minimum pages, using try/except ValueError





