EX\_16OCT - Hiking Trail Elevation Analyzer



Scenario: You recorded your elevation (in meters) at each checkpoint of a hike. You want to know how much you climbed, how much you descended, and where the toughest part was.



Data to start with:

&#x09;elevations = \[350, 420, 515, 490, 610, 680, 655, 720, 700, 640, 580, 600]



Tasks:

&#x20;- Changes between checkpoints. Use a list comprehension to build a list of the differences between each checkpoint and the previous one. For example, the first difference is 420 - 350 = 70. (Hint: range(1, len(elevations)) or zip(elevations, elevations\[1:]) will help.)

&#x20;- Total climb and total descent.

&#x09;Total climb: the sum of all positive changes.

&#x09;Total descent: the sum of all negative changes, shown as a positive number.

&#x20;- Highest and lowest point. Print the highest elevation and the checkpoint number where it occurred. Use enumerate() and start counting checkpoints from 1.

&#x20;- Steepest climb. Find the biggest single positive change and print between which two checkpoints it happened. For example: Steepest climb: +95 m between checkpoint 2 and 3.

&#x20;- Trail profile. Using enumerate(), print one line per segment with an arrow showing the direction:

&#x09;↑ if you went up

&#x09;↓ if you went down

&#x09;→ if there was no change

&#x20;- Difficulty rating (if/else) based on total climb:

&#x09;Under 200 m: Easy

&#x09;200 to 400 m: Moderate

&#x09;Over 400 m: Hard



Bonus (optional):

&#x20;- Put the logic into functions, for example get\_changes(elevations) and rate\_difficulty(total\_climb).

&#x20;- Count how many segments were uphill, downhill, or flat.

