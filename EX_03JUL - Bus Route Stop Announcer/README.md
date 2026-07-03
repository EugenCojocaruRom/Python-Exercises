EX\_03JUL - Bus Route Stop Announcer

You're building the display board for a city bus. The bus has a fixed route with several stops, and you need to show passengers the upcoming stops.



Requirements:

&#x20;- Store the route as a list of stop names, e.g.:

&#x09;route = \["Central Station", "Library", "Market Square", "Hospital", "University", "Stadium", "Airport"]



&#x20;- Ask the user which stop the bus is currently at (they can type the stop name).

&#x20;- Using enumerate(), find the index of that stop in the route.

&#x20;- Print all the remaining stops (everything after the current one), each numbered by how many stops away it is. For example, if the bus is at "Market Square":



&#x20;  1 stop away: Hospital

&#x20;  2 stops away: University

&#x20;  3 stops away: Stadium

&#x20;  4 stops away: Airport



&#x20;- Using a list comprehension, build a separate list containing only the remaining stops whose names are longer than 6 characters.

&#x20;- If the entered stop isn't found in the route, print a friendly error message (don't crash).

&#x20;- If the bus is already at the last stop, print a message like "Final stop reached — no more stops ahead." instead of an empty list.



Bonus (optional):

&#x20;- Let the user also enter a travel time per stop (e.g. 3 minutes), and calculate the estimated arrival time for each upcoming stop.

