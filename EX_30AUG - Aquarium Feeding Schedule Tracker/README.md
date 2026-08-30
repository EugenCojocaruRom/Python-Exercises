EX\_30AUG - Aquarium Feeding Schedule Tracker

Write a program that tracks feeding entries for aquarium tanks. For each entry, collect:

&#x20;- Tank name (letters/spaces only, no empty input)

&#x20;- Fish species being fed

&#x20;- Amount of food in grams (positive number)



Ask the user how many feeding entries to log, then loop and collect that data using while True / try-except validation loops.



Requirements:

&#x20;- Store each entry as a tuple: (tank\_name, species, grams)

&#x20;- Print a numbered feeding log using enumerate(start=1)

&#x20;- Calculate the total grams of food used across all entries

&#x20;- Use a list comprehension to filter entries where grams fed is over 50g ("heavy feedings") — handle singular/plural/zero phrasing like usual

&#x20;- Find the tank with the single largest feeding using max() + lambda, handling ties (list all tied entries)



Bonus:

&#x20;- Aggregate total grams fed per tank using a dictionary, then print a sorted() leaderboard (descending) of which tanks eat the most overall.

