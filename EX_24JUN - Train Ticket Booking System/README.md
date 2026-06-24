EX\_24JUN - Train Ticket Booking System

You're building a simple booking system for a train with a fixed number of seats.



Requirements:

&#x20;- Start with a list representing seats, e.g. seats = \[False] \* 20 (False = empty, True = booked).

&#x20;- Let the user repeatedly choose an action from a menu:

&#x09;-> Book a seat (they pick a seat number)

&#x09;-> Cancel a booking (they pick a seat number)

&#x09;-> View seat map (show all seats, booked vs. free — get creative with how you display it)

&#x09;-> Quit

&#x20;- Use input validation — don't let the user crash the program by typing a letter instead of a number, or picking a seat number that doesn't exist.

&#x20;- When booking, don't allow double-booking an already-booked seat.

&#x20;- Use enumerate() somewhere when displaying the seat map (so you can show seat numbers alongside their status).

&#x20;- Use a list comprehension somewhere — for example, counting how many seats are free, or building a list of all free seat numbers.



Stretch goals (optional):

&#x20;- Show a summary at the end: total booked, total free, occupancy percentage.

&#x20;- Add a "block of seats" booking option (book 2+ adjacent seats together, e.g. for groups).

