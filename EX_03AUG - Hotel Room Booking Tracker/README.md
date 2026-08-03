EX\_03AUG - Hotel Room Booking Tracker

Build a program that tracks guest room bookings for a small hotel.



Core requirements:

&#x20;- Let the user enter bookings dynamically (loop until they type done): guest name, room type (e.g. Single/Double/Suite), number of nights, price per night.

&#x20;- Store each booking as a tuple (or however you like) in a list.

&#x20;- Print a numbered list of all bookings using enumerate() — include the total cost for each booking (nights × price/night).

&#x20;- Calculate and print the total revenue across all bookings using a list comprehension + sum().

&#x20;- Use a list comprehension to find all long-stay guests (staying more than, say, 3 nights) — print them with correct singular/plural wording ("1 night" vs "3 nights").

&#x20;- Use max() with a lambda to find the most expensive booking (guard against the empty-list case).



Bonus:

&#x20;- Aggregate total revenue per room type into a dictionary, then print a sorted() leaderboard (highest revenue first).

&#x20;- Add input validation with while True / try-except for nights and price per night.

