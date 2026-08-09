EX\_09AUG - Pet Grooming Salon Appointment Tracker



Tasks:

&#x20;- Ask the user, in a loop, to enter appointments one at a time: pet name, groom type (e.g. "Bath", "Full Groom", "Nail Trim"), and price. Use 'while True' with a way to stop entering (e.g. typing "done" for the pet name).

&#x20;- Validate the price is a positive number (try/except or a validation loop).

&#x20;- Store each appointment as a tuple: (pet\_name, groom\_type, price).

&#x20;- Print a numbered appointment list using enumerate() starting at 1.

&#x20;- Use a list comprehension to calculate the total revenue for the day.

&#x20;- Use a list comprehension to filter appointments where groom\_type == "Full Groom", and print them with correct singular/plural phrasing (e.g. "1 Full Groom today" vs "3 Full Grooms today").

&#x20;- Use max() with a lambda to find the most expensive appointment — remember to guard against an empty list.



Bonus (optional):

Build a dictionary aggregating total revenue per groom type, then print a leaderboard sorted by revenue descending

