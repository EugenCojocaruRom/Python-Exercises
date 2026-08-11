EX\_11AUG - Karaoke Night Song Queue Tracker

Setup: A karaoke bar wants to track the songs people sign up to sing during the night.



Requirements:

&#x20;- Ask the host how many singers want to perform tonight (positive whole number).

&#x20;- For each singer, collect:

&#x09;Singer's name

&#x09;Song title

&#x09;Song duration in seconds (whole number, must be positive)

&#x20;- Store each entry as a tuple: (name, song, duration).

&#x20;- Print a numbered queue (use enumerate(), starting at 1) showing each singer and their song, e.g.:

&#x20;  1. Ana will sing "Yesterday"

&#x20;  2. Mihai will sing "Bohemian Rhapsody"

&#x20;- Using list comprehension, calculate the total duration of the whole night in seconds, then convert it to minutes and seconds for a friendly readout (something like "Total runtime: 14 min 32 sec").

&#x20;- Using list comprehension, build a list of "long songs" — any song over 240 seconds (4 minutes) — and print how many there are, with correct singular/plural wording ("1 long song" vs "3 long songs").

&#x20;- Find the longest song of the night using max() with a lambda, and print who's singing it (guard against an empty list, in case something goes wrong).



Bonus (optional):

&#x20;- Build a dictionary that counts how many songs each singer signed up for (in case someone queues more than once), then print a leaderboard sorted by song count, descending.

