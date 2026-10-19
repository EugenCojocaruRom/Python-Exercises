EX\_19OCT - Temperature Log Highs and Lows

Scenario: A small weather station records the daily high temperature (in °C) for one week. You’ll write a short program to analyze the readings.



Starting data:

&#x09;days = \["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

&#x09;temps = \[18, 21, 19, 25, 23, 17, 22]



Tasks:

&#x20;- Use enumerate() to print each day with its temperature, numbered from 1, in this format:

&#x09;1. Mon: 18°C

&#x20;- Find and print the hottest and coldest day (name and temperature).

&#x20;- Using a list comprehension, create a list of only the days where the temperature was above the weekly average. Print the average (rounded to 1 decimal) and that list.

&#x20;- Using another list comprehension, create a list of the temperatures converted to Fahrenheit (F = C \* 9/5 + 32), rounded to 1 decimal, and print it.



Hints:

&#x20;- enumerate(days, start=1) gives you the numbering.

&#x20;- max() and min() work on lists, and list.index(value) tells you the position of a value.

&#x20;- zip(days, temps) can help in the list comprehension for task 3.



Bonus (optional): Also print how many days were above 20°C.

