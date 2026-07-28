EX\_27JUL - Book Club Reading Tracker

Your book club is reading a 320-page book together, and everyone logs their progress weekly.



Requirements:

&#x20;- Store each member as a tuple: (name, pages\_read). Ask for dynamic input — how many members, then each member's name and current pages read.

&#x20;- Use enumerate() to print a numbered roster showing each member's name and pages read so far.

&#x20;- Calculate each member's completion percentage (pages\_read / 320 \* 100), and store it somewhere so you can reference it later (dict or list of tuples).

&#x20;- Use a list comprehension to build a list of members who are behind schedule — let's say "behind" means under 50% done.

&#x20;- Use sorted() with a lambda key to print a leaderboard, ranking members from most pages read to least.

&#x20;- Print the average completion percentage across the whole club.



Bonus (optional):

&#x20;- Handle the edge case where someone reports more pages than the book has (320) — flag it as invalid input rather than letting it break your percentage math.

&#x20;- Add a "days until meeting" input, and calculate how many pages per day each behind-schedule member needs to read to catch up by the meeting.

