EX\_21MAY - Vending machine

You have a dictionary of items and their prices.

The user enters coins one at a time (e.g. 10, 50, 1) until they've inserted enough to buy something, then they pick an item.

Write a program that:

&#x20;- Shows the menu with enumerate() (numbered list with prices)

&#x20;- Lets the user insert coins in a loop until their total ≥ the cheapest item

&#x20;- Asks the user to pick an item by number

&#x20;- Uses if/else to either dispense the item + print change owed, or say they haven't inserted enough yet and keep collecting coins

&#x20;- Uses a list comprehension somewhere - e.g. to filter which items the user can afford with their current balance

