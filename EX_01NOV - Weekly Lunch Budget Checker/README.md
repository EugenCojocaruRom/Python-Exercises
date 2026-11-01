EX\_01NOV - Weekly Lunch Budget Checker

Goal: Check how your lunch spending went this week and flag the days you went over budget.



Starter data:



days = \["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

prices = \[8.50, 12.00, 6.75, 15.25, 9.00]

daily\_budget = 10.00



Tasks:

&#x20;- Use enumerate() to loop over prices and print one line per day, like:

&#x09;Monday: $8.50 - OK

&#x09;or Tuesday: $12.00 - OVER by $2.00

&#x20;- Use a list comprehension to build a list of only the prices that went over budget.

&#x20;- Calculate and print:

&#x09;the total spent for the week

&#x09;the average spent per day

&#x09;how many days were over budget

&#x20;- Compare the total to the weekly budget (daily\_budget \* 5) and print one of these:

&#x09;Under budget by $X or

&#x09;Over budget by $X



Expected output (for the data above):

&#x09;Monday: $8.50 - OK

&#x09;Tuesday: $12.00 - OVER by $2.00

&#x09;Wednesday: $6.75 - OK

&#x09;Thursday: $15.25 - OVER by $5.25

&#x09;Friday: $9.00 - OK

&#x09;Over-budget prices: \[12.0, 15.25]

&#x09;Total: $51.50

&#x09;Average: $10.30

&#x09;Days over budget: 2

&#x09;Over budget by $1.50



Hints:

&#x20;- enumerate(prices) gives you an index, which you can use to get the day name from days.

&#x20;- Format money with f-strings: f"{value:.2f}".



Bonus (optional): Print the name of the most expensive day using max() and .index().

