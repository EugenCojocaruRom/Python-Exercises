EX\_12AUG - Vinyl Record Shop Order Tracker

A record shop wants to track the day's orders.



Requirements:

&#x20;- Ask the user how many orders were placed today (validate it's a positive integer — use a while True / try-except loop).

&#x20;- For each order, collect:

&#x09;Customer name (don't allow empty input)

&#x09;Album title

&#x09;Price (validate it's a positive number)

&#x20;- Store each order as a tuple, and keep all orders in a list.

&#x20;- Print a numbered receipt of all orders using enumerate(start=1).

&#x20;- Using a list comprehension, calculate the total revenue for the day.

&#x20;- Using a list comprehension, filter and print all orders over $25 ("premium orders"), with correct singular/plural phrasing depending on how many there are (0 / 1 / many).

&#x20;- Find the most expensive order with max() and a lambda, guarded against an empty list.



Bonus (optional):

&#x20;- Build a dictionary aggregating total spend per customer (in case someone orders more than once), then print a leaderboard sorted by spend, descending, using sorted() with a lambda.

