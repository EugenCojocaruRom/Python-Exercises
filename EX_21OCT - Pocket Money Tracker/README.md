EX\_21OCT - Pocket Money Tracker

Scenario: You’ve written down your daily spending for one week as a list of tuples: (day, category, amount). Write a small program that summarizes it.



Starting data:

expenses = \[

&#x20;   ("Mon", "food", 12.50),

&#x20;   ("Mon", "transport", 3.00),

&#x20;   ("Tue", "food", 8.75),

&#x20;   ("Wed", "fun", 15.00),

&#x20;   ("Wed", "food", 10.25),

&#x20;   ("Thu", "transport", 3.00),

&#x20;   ("Fri", "fun", 22.50),

&#x20;   ("Sat", "food", 18.00),

&#x20;   ("Sun", "fun", 9.00),

]



Tasks:

&#x20;- Print every expense, numbered. Use enumerate() starting at 1, in this format:

&#x09;1. Mon - food: 12.50

&#x20;- Total spent. Use a list comprehension to pull out just the amounts, then use sum().

&#x20;- Food only. Use a list comprehension to build a list of the amounts spent on "food", and print how much that was in total.

&#x20;- Biggest expense. Find the single largest expense and print its day, category, and amount.

&#x20;- Big spender days. Use a list comprehension to build a list of the expenses that cost more than 10. Print how many there are.

&#x20;- Verdict. If the total spent is over 100, print "Over budget!", otherwise print "Within budget."



Expected output for task 2 (as a check): the total should be 101.99... or close to it. Calculate it yourself and see if your number matches!



Bonus (optional): Print the average spent per expense, rounded to 2 decimals.

