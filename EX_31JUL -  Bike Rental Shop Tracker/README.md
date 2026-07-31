EX\_31JUL - Bike Rental Shop Tracker

A bike rental shop wants to track today's rentals and get some quick stats at closing time.



Requirements:

&#x20;- Ask the user to enter rentals one at a time — each rental needs a customer name and a number of hours rented. Keep collecting until they type stop to finish.

&#x20;- Store each rental as a tuple: (customer\_name, hours).

&#x20;- Print a numbered rental log using enumerate() (starting at 1)

&#x20;- The rental rate is $4/hour. Calculate and print each rental's cost, plus the total revenue for the day.

&#x20;- Using a list comprehension, find all rentals of 4+ hours ("long rentals").

&#x20;- Find the customer with the longest rental and the customer with the shortest rental (using max()/min() with a lambda), with a guard against an empty rental list.

&#x20;- Print the total number of rentals.



Bonus (optional):

&#x20;- Group rentals by customer name into a dictionary (in case someone rents more than once during the day), and show a per-customer total cost — sorted highest to lowest.

&#x20;- Add a simple discount rule: if a single rental is 6+ hours, apply a 10% discount to that rental's cost.

