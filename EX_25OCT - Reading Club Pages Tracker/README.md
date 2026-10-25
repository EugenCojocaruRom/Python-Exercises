EX\_25OCT - Reading Club Pages Tracker

Scenario: A small reading club keeps a record of how many pages each member read this week. You’ll write a short program to summarize it.

Tasks:

&#x20;- Print each member’s pages using enumerate(), numbered starting from 1:

&#x20;  1. Ana read 120 pages

&#x20;  2. Bogdan read 45 pages

&#x20;  ...

&#x20;- Calculate and print the total pages and the average pages per member (rounded to 1 decimal place).

&#x20;- Use a list comprehension to build a list of the names of members who read more than the average. Print it.

&#x20;- Use a list comprehension to build a list of “status labels” for every member, following these rules:

&#x09;150 pages or more → "Bookworm"

&#x09;50 to 149 pages → "Reader"

&#x09;fewer than 50 pages → "Just starting"

&#x09;(Hint: you can put an if/else inside a list comprehension, or use a small helper function.)

&#x20;- Print the final report, combining names and labels, for example:

&#x20;  Ana: Reader

&#x20;  Bogdan: Just starting

&#x20;  ...



&#x09;(Hint: zip(members, labels) is handy here, but you can also use enumerate() and index into the lists.)



Bonus (optional): Find the member who read the most pages and print their name. Try doing it without using max() on the names directly, for example by using pages.index(...).

