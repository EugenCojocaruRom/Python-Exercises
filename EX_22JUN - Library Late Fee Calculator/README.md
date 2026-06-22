EX\_22JUN - Library Late Fee Calculator

You're tracking books that have been checked out from a library. Each book has a title and the number of days it's overdue (0 if not overdue).

Requirements:

&#x20;- Store a list of books, where each book is a tuple: (title, days\_overdue)

&#x20;- The late fee is $0.25 per day overdue — no fee if days\_overdue is 0

&#x20;- Print a numbered list (using enumerate()) showing each book's title and its fee, formatted like:



&#x20;  1. The Hobbit          - $0.00

&#x20;  2. Dune                - $3.25

(title left-aligned/padded, fee formatted to 2 decimals)



&#x20;- Use a list comprehension to build a list of only the overdue books' titles

&#x20;- Print the total fees owed across all books



Bonus (optional):

&#x20;- Print which book has the highest fee (using max() with a lambda)

&#x20;- Add a tier: if days\_overdue > 14, it's a "Lost Book Fee" flat $15 instead of the per-day rate

