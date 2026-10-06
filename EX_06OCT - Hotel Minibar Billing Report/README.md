EX\_06OCT - Hotel Minibar Billing Report

Scenario: A hotel keeps a log of minibar items taken by guests during their stay. At checkout, you need to produce a bill and a small summary.



Starting data:



prices = {

&#x20;   "water": 2.50,

&#x20;   "cola": 3.00,

&#x20;   "chips": 4.50,

&#x20;   "chocolate": 3.75,

&#x20;   "beer": 5.00,

&#x20;   "wine": 12.00,

}



\#(room\_number, item) – one entry per item taken

log = \[

&#x20;   (101, "water"), (102, "beer"), (101, "chips"), (103, "cola"),

&#x20;   (102, "beer"), (101, "water"), (103, "wine"), (102, "chocolate"),

&#x20;   (101, "cola"), (103, "juice"), (102, "water"), (103, "chips"),

]



Tasks:

&#x20;- Print a bill per room. For each room (in ascending order), print the items taken with quantities and the room total, for example:

&#x20;  Room 101: 2 x water, 1 x chips, 1 x cola -> 12.00

&#x20;- Handle unknown items. "juice" is not in the price list. Don't crash. Skip it in the totals, and at the end print a warning listing the unknown items.

&#x20;- Apply a discount. If a room's total is 20.00 or more, apply a 10% discount and print both the original and the discounted total.

&#x20;- Final summary. Print:

&#x09;-> the total revenue for all rooms (after discounts)

&#x09;-> the room with the highest bill

&#x09;-> the most popular item overall (the one taken most times)



Requirements:

&#x20;- Use at least one list comprehension (for example, to filter the log for one room).

&#x20;- Use enumerate() at least once (for example, to number the rooms in the final report: 1. Room 101 ...).

&#x20;- Round money to 2 decimals.



Hints:

&#x20;- Build a dictionary like {room: \[items]} first, then work from that.

&#x20;- dict.get(key, default) is handy for counting.

&#x20;- max() accepts a key= argument.



Bonus (optional): Add a 5.00 "service fee" to any room that took 4 or more items, applied before the discount.

