EX\_05OCT - Secret Santa Draw

Goal: Randomly assign each person in a group a "gift recipient" so that nobody draws themselves.



Tasks:

&#x20;- Shuffle: Make a shuffled copy of the list of participants (use random.shuffle() on a copy, so the original stays unchanged).

&#x20;- Pair them up: Assign each person the next person in the shuffled list as their recipient. The last person gives to the first one, so it forms a closed circle. This guarantees nobody draws themselves. Store the result in a dictionary like {"Ana": "Dan", ...}.

&#x20;- Print the result in a numbered format using enumerate(), starting at 1:

&#x20;  1. Ana gives a gift to Dan

&#x20;  2. Bogdan gives a gift to Elena

&#x20;  ...

&#x20;- Validate: Use a list comprehension to build a list of any people who were assigned to themselves. Print "Draw is valid!" if the list is empty, or a warning otherwise.

&#x20;- Count check: Verify that every participant receives exactly one gift. For example, check that len(set(assignments.values())) == len(participants).



Hints:

&#x20;- import random at the top.

&#x20;- To copy a list: shuffled = participants\[:] or participants.copy().

&#x20;- For the circle, think about the index (i + 1) % len(shuffled). The modulo % makes the last person wrap around to index 0.



Bonus (optional):

&#x20;- Add a rule: couples can't draw each other. For example, couples = \[("Ana", "Bogdan"), ("Cristina", "Dan")]. If a draw breaks the rule, reshuffle and try again using a while loop.

&#x20;- Let the user type the names (comma-separated) instead of using a fixed list.

