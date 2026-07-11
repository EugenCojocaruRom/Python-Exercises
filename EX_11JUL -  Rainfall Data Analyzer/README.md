EX\_11JUL - Rainfall Data Analyzer

You have a list of daily rainfall amounts (in mm) for a week:

&#x09;rainfall = \[3.2, 0.0, 12.5, 7.8, 0.0, 0.0, 5.1]



Write a program that:

&#x20;- Calculates and prints the average rainfall for the week.

&#x20;- Uses a list comprehension to build a list of the days (as day numbers, 1–7) where rainfall was above average.

&#x20;- Uses enumerate() to print each day with its rainfall amount, formatted like:



&#x20;  Day 1: 3.2 mm

&#x20;  Day 2: 0.0 mm

&#x20;  ...



&#x20;- Finds the longest streak of consecutive dry days (rainfall == 0.0) and prints how many days that streak lasted.



Bonus (optional): Ask the user to input 7 rainfall values themselves instead of using the hardcoded list, with basic validation (must be a non-negative number).

