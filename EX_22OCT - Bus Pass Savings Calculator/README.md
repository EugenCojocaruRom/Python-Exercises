EX\_22OCT - Bus Pass Savings Calculator

Scenario: A city sells a monthly bus pass for $40. A single ride costs $2.50. You have a list of how many rides a commuter took each week over several weeks, and you want to know whether the pass would have saved them money.



Sample data:

&#x09;weekly\_rides = \[8, 12, 5, 14, 10, 9, 11, 6]



Tasks:

&#x20;- Total rides: Calculate the total number of rides taken across all weeks.

&#x20;- Weekly cost: Using a list comprehension, create a list with the cost of each week if paid per ride (rides × $2.50).

&#x20;- Print a weekly table using enumerate() (start the week numbers at 1), for example:

&#x20;  Week 1: 8 rides -> $20.00

&#x20;  Week 2: 12 rides -> $30.00

&#x20;- Compare: Add up the weekly costs and compare to the $40 pass. Print one of these messages:

&#x09;Pass would have saved you $X.XX (if the pass is cheaper)

&#x09;Pay-per-ride was cheaper by $X.XX (if pay-per-ride is cheaper)

&#x09;Both options cost the same (if equal)

&#x20;- Busy weeks: Using another list comprehension, create a list of the week numbers where the commuter took more than 9 rides, and print it.



A note on the data

The data covers 8 weeks, but the pass is monthly. For this exercise, just compare the total pay-per-ride cost against one $40 pass. Treat it as a simplified model, and don’t worry about the mismatch.



Bonus (optional)

Find the break-even point: how many rides would make the pass exactly as cheap as pay-per-ride? (Hint: $40 ÷ $2.50.) Print it.

