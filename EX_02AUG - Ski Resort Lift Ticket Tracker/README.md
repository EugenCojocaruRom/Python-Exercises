EX\_02AUG - Ski Resort Lift Ticket Tracker

Goal: Track lift ticket sales at a ski resort and generate a summary report.



Requirements:

&#x20;- Let the user enter ticket sales one at a time (customer name + ticket type e.g. "Full Day", "Half Day", "Season Pass" + price). Keep collecting until they type done for the customer name.

&#x20;- Store each sale as a tuple: (customer\_name, ticket\_type, price).

&#x20;- Print a numbered summary of all sales using enumerate() (start at 1), formatted like:

&#x20;  1. Radu - Full Day - $65.00

&#x20;  2. Elena - Half Day - $40.00

&#x20;- Calculate and print the total revenue for the day.

&#x20;- Use a list comprehension to find all "Season Pass" sales and print how many were sold.

&#x20;- Use max() with a lambda to find the highest-priced sale — guard against a ValueError if no sales were entered.



Bonus (optional):

&#x20;- Tally total revenue per ticket type using a dictionary, then print it sorted from highest to lowest revenue.

