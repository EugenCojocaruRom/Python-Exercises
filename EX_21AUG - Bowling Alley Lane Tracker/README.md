EX\_21AUG - Bowling Alley Lane Tracker

A bowling alley wants to track lane rentals for the night.



Requirements:

&#x20;- Ask how many groups are renting a lane tonight (validate it's a positive integer).

&#x20;- For each group, collect:

&#x09;Group name (non-empty)

&#x09;Number of players (positive integer)

&#x09;Hours renting the lane (positive number, can be a decimal like 1.5)

&#x20;- Each lane costs $25/hour, plus a $5 shoe rental fee per player.

&#x20;- Store each group's info in a tuple (name, players, hours, total cost).

&#x20;- Print a numbered list (use enumerate() with start=1) showing each group's name, players, hours, and total cost.

&#x20;- Print the total revenue for the night.

&#x20;- Use a list comprehension to find groups renting for 2+ hours ("long sessions") — print how many there are, with correct singular/plural wording (and handle the zero case).

&#x20;- Use max() with a lambda to find the group that spent the most — handle ties if you want an extra challenge, and guard against an empty list.



Bonus (optional): Aggregate total players served across all groups, and print the average cost per group.

