EX\_22SEP - Pharmacy – Expired Stock Checker

You have a list of medicines from a pharmacy, each represented as a tuple (name, quantity, days\_until\_expiry).



Requirements:

&#x20;- Using enumerate(), print each medicine along with its position in the list (position 1, 2, 3...).

&#x20;- Using a list comprehension, build a list of the names of medicines that expire in less than 10 days (days\_until\_expiry < 10).

&#x20;- Using another list comprehension, build a list of the names of medicines that are out of stock (quantity is 0).

&#x20;- Calculate how many medicines need "urgent restocking" — meaning quantity below 15 or expiring in less than 10 days.

&#x20;- At the end, print a message like: "Warning: 3 medicines need urgent restocking!"



Bonus (optional): sort the list of medicines by days\_until\_expiry, ascending, using sorted() and a lambda.

