EX\_10SEP - Music Store Instrument Rental Tracker

A music shop rents out instruments and wants to track daily rentals.



Core requirements:

&#x20;- Ask the user how many rentals to log today (validate it's a positive integer).

&#x20;- For each rental, collect:

&#x09;Customer name

&#x09;Instrument type (e.g., Guitar, Violin, Drums, Keyboard — validate against an allowed list, case-insensitive)

&#x09;Rental price (validate it's a positive number)

&#x20;- Store each rental as a tuple: (customer\_name, instrument, price).

&#x20;- Print a numbered list of all rentals using enumerate(), starting at 1.

&#x20;- Calculate and print the total revenue from all rentals.

&#x20;- Using a list comprehension, filter and display all rentals priced over $50, with correct singular/plural/zero phrasing (e.g., "1 rental over $50" vs "3 rentals over $50" vs "No rentals over $50").

&#x20;- Find the most expensive rental using max() + lambda. Handle ties by showing all of them (list comprehension).



Bonus (optional):

&#x20;- Build a dictionary aggregating total revenue per instrument type, then print a leaderboard sorted by revenue descending (sorted() + lambda).

&#x20;- Add a percentage-of-total-revenue column per instrument, formatted to 1 decimal place.

