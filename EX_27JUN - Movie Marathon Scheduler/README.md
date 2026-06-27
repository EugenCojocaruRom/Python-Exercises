EX\_27JUN - Movie Marathon Scheduler

You're planning a movie marathon night and want a tool to figure out scheduling.

Requirements:



&#x20;- Create a list of movies, where each movie is a tuple: (title, duration\_in\_minutes). Make at least 5 movies.

&#x20;- Print a numbered list of all movies (use enumerate()), showing title and duration.

&#x20;- Calculate and print the total runtime of all movies combined, formatted as hours and minutes (e.g., "Total runtime: 8h 45m").

&#x20;- Using list comprehension, create a list of just the titles of movies that are longer than 100 minutes.

&#x20;- Find and print the longest movie and the shortest movie (title + duration).

&#x20;- Ask the user for a "start time" (just the hour, 0-23, as an integer) and calculate what hour the marathon would end at, accounting for rolling past midnight (e.g., if it starts at 22 and runs 5 hours, it should say it ends at 3, not 27). Use the modulo operator % for this.



Bonus (optional):

&#x20;- Sort the movies by duration (shortest to longest) before displaying them.

&#x20;- Let the user input how many "break minutes" they want between movies, and add that to the total runtime calculation.

