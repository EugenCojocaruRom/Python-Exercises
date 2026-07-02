EX\_02JUL - Weekly Chore Rotation Assigner

You have a list of roommates and a list of chores. Each week, chores rotate to the next person using modulo math, so nobody gets stuck with dishes forever.



Requirements:

&#x20;- Create a list of roommates (e.g. \["Ana", "Mihai", "Diana", "Radu"]) and a list of chores (e.g. \["Dishes", "Trash", "Vacuum", "Laundry"]).

&#x20;- Ask the user to input a week number (e.g. 3).

&#x20;- For that week, assign each chore to a roommate using rotation logic — chore i goes to roommate (i + week\_number) % len(roommates).

&#x20;- Print the assignment nicely using enumerate(), like:



&#x20;  Week 3 Chore Assignments:

&#x20;  Dishes  -> Diana

&#x20;  Trash   -> Radu

&#x20;  Vacuum  -> Ana

&#x20;  Laundry -> Mihai



&#x20;- Use a list comprehension somewhere — for example, to build the list of (chore, roommate) pairs before printing them.



Bonus (optional):

&#x20;- Let the user enter multiple week numbers and show how the rotation changes over time.

&#x20;- Align the chore names using dynamic f-string padding.

