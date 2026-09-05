EX\_05SEP - Food Pantry Donation Tracker

A food pantry wants to track incoming donations for the day.



Core requirements:

&#x20;- Ask the user how many donations were dropped off today (validate it's a positive integer).

&#x20;- For each donation, collect:

&#x09;Donor name (validate letters/spaces only)

&#x09;Food item (e.g. "canned soup", "rice", "pasta")

&#x09;Weight in kg (validate it's a positive number)

&#x20;- Store each donation as a tuple: (donor\_name, item, weight).

&#x20;- Print a numbered list of all donations using enumerate() (start at 1).

&#x20;- Calculate and print the total weight donated today.

&#x20;- Using a list comprehension, filter out "heavy donations" — anything over 5kg — and print them with correct singular/plural/zero phrasing.

&#x20;- Find the single heaviest donation using max() with a lambda, and handle ties (more than one donation at the max weight) by listing all of them.



Bonus (optional):

&#x20;- Build a dictionary aggregating total weight donated per food item, then print a sorted() leaderboard from heaviest total to lightest.

&#x20;- Add a simple "pantry capacity" check: if total weight exceeds, say, 50kg, print a message that the pantry is full for the day.

