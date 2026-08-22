EX\_22AUG - Barbershop Appointment Tracker

Build a program that tracks a barbershop's appointments for the day.



&#x20;- Ask the barber how many appointments they have today (validate it's a positive whole number).

&#x20;- For each appointment, collect:

&#x09;Customer name

&#x09;Haircut type (e.g. "Buzz Cut", "Fade", "Beard Trim", "Full Package")

&#x09;Duration in minutes (validate it's a positive number)

&#x20;- Store each appointment as a tuple.

&#x20;- Print a numbered list of all appointments using enumerate() (start at 1), showing name, haircut type, and duration.

&#x20;- Using a list comprehension, build a list of "long appointments" — anything over 45 minutes — and print how many there are with correct singular/plural wording ("1 long appointment" vs "3 long appointments"), or a friendly message if there are none.

&#x20;- Calculate and print the total time the barber will spend today (sum of all durations).

&#x20;- Find the longest appointment using max() with a lambda — and make sure it doesn't crash if the appointment list happens to be empty.



Bonus (optional):

&#x20;- Build a dictionary aggregating total minutes spent per haircut type, then print a leaderboard (sorted descending) showing which haircut type eats up the most of the barber's day.

