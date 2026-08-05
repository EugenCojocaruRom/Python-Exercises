EX\_05AUG - Laundromat Machine Usage Tracker

A laundromat wants to track machine usage throughout the day. For each customer, record which machine they used (e.g. "Washer 1", "Dryer 3") and how long they used it for (in minutes).



Requirements:

&#x20;- Let the user enter usage records one at a time (machine name + minutes used) until they type done.

&#x20;- Store each entry as a tuple: (machine\_name, minutes).

&#x20;- Print a numbered list of all usage records (use enumerate() with start=1).

&#x20;- Calculate the total machine-minutes used across all entries.

&#x20;- Use a list comprehension to find all sessions that ran longer than 45 minutes — call these "long cycles" — and print them (handle 0/1/many nicely, singular vs plural).

&#x20;- Find the longest single session using max() with a lambda — guard against an empty list.



Bonus:

&#x20;- Aggregate total minutes used per machine (dictionary), then print a leaderboard of the most-used machines with sorted().

