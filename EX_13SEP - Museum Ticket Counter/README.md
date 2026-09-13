EX\_13SEP - Museum Ticket Counter

A small tracker for a museum's daily visitors.



Base requirements:

&#x20;- Ask how many visitors were recorded (with while True/try-except validation).

&#x20;- For each visitor, collect:

&#x09;name

&#x09;ticket type (Adult, Child, Senior) — validate against these options

&#x09;price paid (number)

&#x20;- Store each visitor as a tuple (name, ticket\_type, price) in a list.

&#x20;- Display the full list using enumerate(start=1).

&#x20;- Calculate and display:

&#x09;total revenue (sum())

&#x09;a list comprehension filtering only Child visitors, with singular/plural/zero message handling.



Bonus:

&#x20;- Find the most expensive ticket sold, handling ties (max() + lambda + list comprehension for all tickets at the max price).

&#x20;- A dictionary of total revenue per ticket type, shown as a leaderboard with sorted() descending, plus each type's percentage of total (:.1f).

