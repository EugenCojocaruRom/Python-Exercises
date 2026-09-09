EX\_09SEP - Planetarium Show Booking Tracker

A planetarium wants to track bookings for its shows.



Requirements:

&#x20;- Ask how many bookings to enter (with input validation).

&#x20;- For each booking, collect: visitor name, show name (e.g., "Journey to Mars", "Northern Lights"), and number of seats booked. Validate as you see fit.

&#x20;- Store each booking as a tuple.

&#x20;- Using enumerate() starting at 1, print a numbered list of all bookings.

&#x20;- Calculate the total number of seats booked across all bookings (use sum() with a generator).

&#x20;- Using a list comprehension, filter and display bookings with 6 or more seats (group bookings) — handle singular/plural and the zero-matches case.

&#x20;- Find the largest booking (most seats) using max() with a lambda — and handle a tie by showing all bookings that share the max, via list comprehension.



Bonus (optional):

&#x20;- Aggregate total seats booked per show into a dictionary, then print a leaderboard (most popular show first) with each show's percentage of total seats booked.

