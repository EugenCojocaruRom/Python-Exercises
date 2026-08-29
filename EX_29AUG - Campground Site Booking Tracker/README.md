EX\_29AUG - Campground Site Booking Tracker



Tasks:

&#x20;- Ask the camper how many bookings they want to enter (validate positive integer).



For each booking, collect:

&#x20;- Camper name (letters/spaces only — validate)

&#x20;- Site type: "Tent", "RV", or "Cabin" (validate against this list)

&#x20;- Number of nights (positive integer)

&#x20;- Site nightly rates: Tent = $15, RV = $35, Cabin = $60. Calculate total cost per booking (nights × rate).

&#x20;- Store each booking as a tuple: (camper\_name, site\_type, nights, total\_cost).

&#x20;- Print a numbered summary of all bookings using enumerate(start=1).

&#x20;- Calculate and print the total revenue across all bookings.

&#x20;- Using a list comprehension, filter and print bookings that stayed 5 nights or more ("long stays") — with singular/plural/zero messaging.

&#x20;- Find the most expensive booking using max() with lambda, handling ties (print all tied bookings).



Bonus:

&#x20;- Aggregate total revenue per site type (Tent/RV/Cabin) into a dictionary, then print a sorted() leaderboard from highest to lowest earning site type.

