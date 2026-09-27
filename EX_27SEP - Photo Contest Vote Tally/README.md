EX\_27SEP - Photo Contest Vote Tally

A local photo contest has several entries. You're given two lists (same order/length):



&#x09;titles = \["Sunset Over Iasi", "Old Castle Ruins", "Morning Fog", "Street Cats", "City Lights"]

&#x09;votes  = \[23, 45, 12, 45, 30]



Tasks:

&#x20;- Print each entry with its position number (starting at 1), like:

&#x09;1. Sunset Over Iasi — 23 votes

&#x20;- Use enumerate() for this instead of manually tracking an index.

&#x20;- Calculate the average number of votes (round to 1 decimal place).

&#x20;- Using a list comprehension, build a list of titles that scored above average.

&#x20;- Find the highest vote count, then — since there could be a tie — use a list comprehension to get all titles that match that highest count (don't assume there's only one winner).

&#x20;- Print a short summary:

&#x20;  Average votes: 31.0

&#x20;  Above average: \['Old Castle Ruins', 'Street Cats']

&#x20;  Winner(s): \['Old Castle Ruins', 'Street Cats']



Bonus (optional): Instead of hardcoding the lists, ask the user to input titles and votes one at a time until they type "done".

