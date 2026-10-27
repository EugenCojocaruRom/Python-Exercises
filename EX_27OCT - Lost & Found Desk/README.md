EX\_27OCT - Lost \& Found Desk

Scenario: A train station keeps a list of items handed in at its lost \& found desk. Each item is stored as a string in the format "item:color:station".



items = \[

&#x20;   "umbrella:black:Iasi",

&#x20;   "backpack:blue:Bucharest",

&#x20;   "wallet:brown:Iasi",

&#x20;   "scarf:red:Cluj",

&#x20;   "phone:black:Iasi",

&#x20;   "umbrella:green:Cluj",

&#x20;   "keys:silver:Bucharest",

&#x20;   "gloves:black:Cluj",

]



Tasks:

&#x20;- Parse the list. Use a list comprehension with .split(":") to turn every string into a list of three parts. For example, "wallet:brown:Iasi" becomes \["wallet", "brown", "Iasi"].

&#x20;- Print a numbered report. Use enumerate() starting at 1, so each line looks like this:

&#x20;  1. umbrella (black) - found at Iasi

&#x20;- Count items per station. Use a dictionary to count how many items were found at each station, then print the counts.

&#x20;- Filter by color. Use a list comprehension to build a list of all item names that are "black", then print it.

&#x20;- Find the busiest station. Print the name of the station with the most items. (Hint: max() with key= works well, but a simple loop is fine too.)

&#x09;Expected output (roughly)

&#x09;1. umbrella (black) - found at Iasi

&#x09;2. backpack (blue) - found at Bucharest

&#x09;...



&#x09;Items per station:

&#x09;Iasi: 3

&#x09;Bucharest: 2

&#x09;Cluj: 3



&#x09;Black items: \['umbrella', 'phone', 'gloves']

&#x09;Busiest station: Iasi



&#x09;(If two stations tie, either one is fine for the last line.)



Bonus (optional):

&#x20;- Ask the user to type a station name with input() and print all items found there. Print a friendly message if nothing was found.

