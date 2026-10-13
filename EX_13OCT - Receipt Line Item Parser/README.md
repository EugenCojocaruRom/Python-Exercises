EX\_13OCT - Receipt Line Item Parser

Scenario: A small shop exports receipt lines as messy text. You need to clean them up, total them, and print a tidy report.



Starting data:

raw\_lines = \[

&#x20;   "  apple , 3 , 0.50 ",

&#x20;   "BREAD,1,2.25",

&#x20;   " milk ,2, 1.10",

&#x20;   "apple,2,0.50",

&#x20;   "Cheese , 1 , 4.80 ",

&#x20;   "bread, 2, 2.25",

&#x20;   "",

&#x20;   "banana,6,0.20",

]



Each line has the format name, quantity, unit\_price. Some lines have extra spaces, mixed upper/lower case, or are empty.



Tasks:

&#x20;- Clean and parse. Using a list comprehension (or a loop if you prefer), skip empty lines. For each remaining line, split on commas, strip the spaces, lowercase the name, and convert quantity to int and price to float. Store each item as a tuple (name, quantity, price).

&#x20;- Merge duplicates. Build a dictionary where each key is an item name and each value is the total quantity bought across all lines (for example, apple appears twice, so its total quantity is 5).

&#x20;- Print a numbered report using enumerate() (starting at 1), sorted alphabetically by item name. Each row shows the number, name, total quantity, unit price, and line total e.g.:

&#x09;1. apple     x5   @ 0.50 = 2.50

&#x09;2. banana    x6   @ 0.20 = 1.20

&#x20;- Try to align the columns using f-string formatting, such as f"{name:<8}".

&#x20;- Print a summary at the end:

&#x09;Grand total

&#x09;The most expensive line (name and amount)

&#x09;The number of unique items



Bonus (optional):

&#x20;- Use a list comprehension to build a list of all items whose line total is greater than 2.00.

&#x20;- Add a 10% discount if the grand total is above 15.00, and print both the original and discounted totals.

