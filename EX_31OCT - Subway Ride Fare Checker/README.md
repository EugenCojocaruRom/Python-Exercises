EX\_31OCT - Subway Ride Fare Checker

Scenario: A city subway charges a different fare depending on the time of day. You have a list of rides from one week, and you want to know how much you spent.



Data to start with:



rides = \[

&#x20;   ("Mon", 7, 2.50),

&#x20;   ("Mon", 18, 2.50),

&#x20;   ("Tue", 12, 1.80),

&#x20;   ("Wed", 8, 2.50),

&#x20;   ("Wed", 22, 1.20),

&#x20;   ("Fri", 9, 2.50),

&#x20;   ("Sat", 14, 1.80),

]



Each ride is a tuple: (day, hour, fare), where hour uses the 24-hour clock.



Tasks:

&#x20;- Print each ride on its own line, numbered starting from 1, using enumerate(). Example format: 1. Mon at 7:00 - $2.50

&#x20;- Use a list comprehension to build a list of only the fares.

&#x20;- Calculate and print the total spent and the average fare (rounded to 2 decimals).

&#x20;- Use a list comprehension to find all rides that happened during rush hour (hours 7 to 9, or 17 to 19), and print how many there were.

&#x20;- Using if/elif/else, print a message based on the total:

&#x09;Under $10: "Light week!"

&#x09;$10 to $15: "Normal week."

&#x09;Over $15: "Consider a weekly pass!"



Bonus (optional): Find and print the most expensive ride, including its day and hour.

