EX\_15OCT - Tip Splitter at the Restaurant

Scenario: A group of friends finishes dinner. You have a list of what each person ordered (as a price), and you want to calculate each person’s share including a tip.



Starting data (or make it dynamic):

&#x09;names = \["Ana", "Mihai", "Ioana", "Dan", "Elena"]

&#x09;meals = \[45.50, 62.00, 38.75, 55.20, 70.10]

&#x09;tip\_percent = 15



Tasks:

&#x20;- Use enumerate() to print each person’s meal on its own line, numbered starting from 1, like this:

&#x09;1. Ana ordered a meal costing 45.50

&#x20;- Calculate the total bill (sum of all meals).

&#x20;- Calculate the tip amount (tip\_percent of the total).

&#x20;- Use a list comprehension to build a new list called totals, where each item is that person’s meal plus their own share of the tip (their meal × tip percent).

&#x20;- Print each person’s final amount, rounded to 2 decimals, like this:

&#x09;Ana pays 52.33

&#x20;- Find and print who paid the most and who paid the least.



Bonus (optional): Use a second list comprehension to build a list of only the names of people who paid more than the average.



Hints:

&#x20;- round(number, 2) rounds to 2 decimal places.

&#x20;- max() and min() work on lists, and list.index(value) tells you the position of a value.

&#x20;- An f-string like f"{price:.2f}" also formats numbers to 2 decimals.

