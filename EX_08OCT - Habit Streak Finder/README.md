EX\_08OCT - Habit Streak Finder (Runs of Consecutive Days)

Scenario: You track the days of the month on which you did a workout. Given a sorted list of day numbers, find the longest streak of consecutive days and report it.



Example data:

&#x09;workout\_days = \[1, 2, 3, 5, 6, 9, 10, 11, 12, 15, 20, 21]



Your program should:

&#x20;- Split the days into streaks (groups of consecutive days). For the data above, the streaks are:

&#x09;\[1, 2, 3]

&#x09;\[5, 6]

&#x09;\[9, 10, 11, 12]

&#x09;\[15]

&#x09;\[20, 21]

&#x20;- Print each streak with its number, using enumerate(). Example: Streak 1: days 1-3 (3 days)

&#x20;- Find and print the longest streak. Example: Longest streak: days 9-12 (4 days)

&#x20;- Print the total number of workout days and the number of streaks.



Use a list comprehension at least once. For example, to build a list of the streak lengths.



Hints:

&#x20;- Go through the list with a for loop and compare each day with the previous one. If day == previous + 1, you're continuing the current streak. Otherwise, the streak ended and a new one begins.

&#x20;- Keep a current\_streak list and a streaks list (a list of lists). Don't forget to save the last streak after the loop ends!

&#x20;- max() can take a key= argument, for example max(streaks, key=len).



Bonus (optional):

&#x20;- If two streaks are tied for the longest, print both.

&#x20;- Print the longest gap between workouts (the most days in a row with no workout).

