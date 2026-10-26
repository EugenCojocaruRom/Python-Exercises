EX\_26OCT - Tea Shelf Stock Check

Scenario: A small tea shop keeps its stock in a list of tuples, where each tuple is (tea\_name, grams\_in\_stock).



stock = \[

&#x20;   ("Green", 250),

&#x20;   ("Earl Grey", 40),

&#x20;   ("Chamomile", 0),

&#x20;   ("Peppermint", 120),

&#x20;   ("Jasmine", 15),

&#x20;   ("Black", 300),

]



Tasks:

&#x20;- Numbered list: Use enumerate() (starting at 1) to print every tea like this:

&#x09;1. Green - 250g

&#x20;- Low stock: Use a list comprehension to build a list of the names of teas with less than 50 grams in stock (but still more than 0). Print it.

&#x20;- Out of stock: Use another list comprehension to build a list of the names of teas with 0 grams. Print it.

&#x20;- Total stock: Use a for loop to add up all the grams, and print the total.

&#x20;- Restock message: Use a for loop with if/elif/else to print one line per tea:

&#x09;OK if stock is 50 or more

&#x09;LOW if stock is between 1 and 49

&#x09;EMPTY if stock is 0

&#x09;	Example: Earl Grey: LOW



Bonus (optional): Find and print the name of the tea with the most grams in stock, without using max().

