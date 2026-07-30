EX\_30JUL - Food Truck Order Tracker

A food truck wants to track today's orders and get some quick stats at closing time.



Requirements:

&#x20;- Ask the user to enter orders one at a time — each order needs a customer name and an item price. Keep collecting until they type done (or similar) to stop.

&#x20;- Store each order as a tuple: (customer\_name, price).

&#x20;- Print a numbered receipt of all orders using enumerate() (starting at 1)

&#x20;- Calculate and print the total revenue for the day.

&#x20;- Using a list comprehension, find all orders over $10 (the "big spenders").

&#x20;- Find the most expensive order and the cheapest order (using max()/min() with a lambda).

&#x20;- Print how many orders were placed in total.



Bonus (optional):

&#x20;- Group orders by customer name into a dictionary (in case someone ordered more than once), and show a per-customer total.

&#x20;- Handle the edge case where the food truck had zero orders today (avoid crashing on max()/min() of an empty list).

