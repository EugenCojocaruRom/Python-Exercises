EX\_20OCT - Plant Watering Reminder

Scenario: You have a few houseplants. Each one needs water every certain number of days. Write a small program that tells you which plants need watering today.



Starting data:

plants = \[

&#x20;   ("Cactus", 14, 10),

&#x20;   ("Basil", 2, 3),

&#x20;   ("Fern", 3, 1),

&#x20;   ("Aloe", 10, 12),

&#x20;   ("Mint", 2, 2),

]



Each tuple is (name, water\_every\_n\_days, days\_since\_last\_watering).



Tasks

&#x20;- Loop with enumerate(): Print a numbered list of all plants, starting from 1, in this format:

&#x20;  1. Cactus - water every 14 days

&#x20;- Check each plant: A plant needs water if days\_since\_last\_watering >= water\_every\_n\_days. Print a line for each plant:

&#x09;Basil needs water today!

&#x09;Fern is fine (2 days left)

(Days left = water\_every\_n\_days − days\_since\_last\_watering.)

&#x20;- List comprehension: Build a list called thirsty containing only the names of the plants that need water. Print it.

&#x20;- Summary: Print how many plants need water out of the total, for example: 3 of 5 plants need water.



Bonus (optional)

&#x20;- Find the plant that is the most overdue (the largest value of days\_since\_last\_watering - water\_every\_n\_days) and print its name.

