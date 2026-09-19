EX\_19SEP - Movie Theater Snack Bar Tracker

Write a program that tracks snack orders at a movie theater concession stand.



Requirements:

&#x20;- Ask the user how many orders there are.

&#x20;- For each order, collect:

&#x09;Customer name (letters only)

&#x09;Snack item (e.g., "Popcorn", "Nachos", "Soda", "Candy")

&#x09;Price (a positive number)

&#x20;- Store each order as a tuple: (customer\_name, snack\_item, price).

&#x20;- Using enumerate() starting at 1, print a numbered list of all orders.

&#x20;- Calculate and print the total revenue from all orders.

&#x20;- Use a list comprehension to find all orders over $10, and print them with correct singular/plural wording (and handle the case where there are none).

&#x20;- Find the most expensive order — handle ties (more than one order sharing the top price).



Bonus (optional):

&#x20;- Build a dictionary aggregating total revenue per snack item, then print a leaderboard sorted by revenue (highest first), each with its percentage of total revenue.

