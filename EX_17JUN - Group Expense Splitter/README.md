EX\_17JUN - Group Expense Splitter

The idea: a group of friends went on a trip and paid for different things. You need to figure out who owes money and who should get money back.

Core requirements:

&#x20;- Ask the user how many people are in the group

&#x20;- For each person, collect their name and how much they paid (use a loop with enumerate() somewhere, even if it's just for numbering the inputs nicely)

&#x20;- Calculate the total amount spent and the fair share per person (total ÷ number of people)

&#x20;- For each person, show whether they owe money or should receive money, and how much (their paid amount minus their fair share)

Stretch goals:

&#x20;- Round money values to 2 decimals properly

&#x20;- Use a list comprehension to build the list of balances (paid − fair share) instead of a manual loop

&#x20;- Sort people from "owes the most" to "gets back the most" before printing the summary

&#x20;- Handle the edge case where someone paid exactly their fair share (no owing, no receiving)

