EX\_14AUG - Board Game Café Table Tracker

A board game café wants to track table rentals for the evening.



Requirements:

&#x20;- Ask the user how many tables were rented tonight (validate it's a positive number).

&#x20;- For each table, collect:

Group name

Game they're playing

Number of hours rented (must be a positive number — validate it)

&#x20;- Store each rental as a tuple, in a list.

&#x20;- Print a numbered summary of all rentals using enumerate() (start at 1).

&#x20;- Using a list comprehension, calculate the total hours rented across all tables.

&#x20;- Using another list comprehension, filter out "long sessions" — any rental 3 hours or more — and print them with correct singular/plural wording ("1 long session" vs "3 long sessions").

&#x20;- Find the group that rented for the longest time using max() with a lambda, guarded against an empty list.



Bonus (optional):

&#x20;- Charge $5/hour per table, and print total revenue for the night.

&#x20;- Build a dictionary aggregating total hours played per game (in case the same game gets picked by multiple groups), then print a leaderboard of most-played games using sorted().

