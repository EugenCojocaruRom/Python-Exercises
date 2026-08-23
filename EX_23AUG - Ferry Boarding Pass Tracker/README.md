EX\_23AUG - Ferry Boarding Pass Tracker

A small ferry company wants a program to track passengers boarding for a crossing.



Requirements:

&#x20;- Ask the user how many passengers are boarding (validate it's a positive integer).

&#x20;- For each passenger, collect their name and ticket type ("Standard", "Vehicle", or "VIP") — validate the ticket type against that list.

&#x20;- Store each entry (assign a price: Standard = $15, Vehicle = $45, VIP = $30).

&#x20;- Using enumerate() starting at 1, print a numbered boarding list showing name, ticket type, and price.

&#x20;- Use a list comprehension to calculate the total revenue from all passengers.

&#x20;- Use a list comprehension to build a list of just the VIP passengers (name only), and print it with correct singular/plural/zero phrasing (e.g. "1 VIP passenger" vs "3 VIP passengers" vs "No VIP passengers today").

&#x20;- Find the most expensive ticket sold (handle ties — there could be more than one).



Bonus (optional): The ferry has a capacity of 50 passengers. Track running capacity as people board, and if someone tries to board after the ferry is full, print a "Ferry full" message instead of adding them.

