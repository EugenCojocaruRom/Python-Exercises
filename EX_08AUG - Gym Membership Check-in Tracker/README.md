EX\_08AUG - Gym Membership Check-in Tracker



Tasks:

&#x20;- Let the user enter check-ins one at a time: member name and workout duration (in minutes). Use a while True loop with a sentinel value (e.g. typing "done") to stop, validating that duration is a positive number.

&#x20;- Store each check-in as a tuple: (name, duration).

&#x20;- Print a numbered list of all check-ins using enumerate() (start=1).

&#x20;- Using a list comprehension, calculate the total minutes worked out across all check-ins.

&#x20;- Using a list comprehension, find all "long sessions" — any check-in over 60 minutes — and print them with correct singular/plural messaging ("1 long session" vs "3 long sessions"), including a clean message for zero.

&#x20;- Use max() with a lambda key to find the longest single session, guarded against an empty list (in case the user quits with no entries).



Bonus: Aggregate total minutes per member in a dictionary (a member might check in more than once), then print a leaderboard sorted by total minutes descending — who's the most dedicated gym-goer?

