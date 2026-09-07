EX\_07SEP - Recycling Center Drop-off Tracker

A recycling center wants to track drop-offs throughout the day.



Requirements:

&#x20;- Ask the user how many drop-offs happened today (validate it's a positive integer).

&#x20;- For each drop-off, collect:

&#x09;Person's name (letters only — reuse your usual validation pattern)

&#x09;Material type (e.g. "Plastic", "Glass", "Paper", "Metal")

&#x09;Weight in kg (validate it's a positive number)

&#x20;- Store each drop-off as a tuple.

&#x20;- Print a numbered list of all drop-offs using enumerate() (e.g. 1. Eugen dropped off 4.5kg of Plastic).

&#x20;- Using a list comprehension, calculate the total weight recycled today.

&#x20;- Using a list comprehension, filter and display "heavy drop-offs" — anything over 10kg — with correct singular/plural/zero messaging.

&#x20;- Find the largest single drop-off (by weight), handling ties (more than one person could've dropped off the same max weight).



Bonus:

&#x20;- Aggregate total weight recycled per material type into a dictionary, then print a sorted leaderboard (descending) showing which material had the most weight recycled.

&#x20;- Extra bonus: calculate what percentage of today's total weight each material type represents.

