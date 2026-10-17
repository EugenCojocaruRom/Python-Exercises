EX\_17OCT - Duplicate Email Cleaner

Scenario: You’re given a mailing list full of email addresses. Some are duplicates that differ only by capitalization or extra spaces. Clean the list, remove the duplicates, and report what you found.



Starting data:

emails = \[

&#x20;   "Anna@Example.com",

&#x20;   "  bob@example.com",

&#x20;   "anna@example.com ",

&#x20;   "carol@Example.com",

&#x20;   "BOB@example.com",

&#x20;   "dave@example.com",

&#x20;   "carol@example.com",

&#x20;   "eve@example.com  ",

]



Tasks:

&#x20;- Clean each email. Remove leading and trailing spaces (.strip()) and convert to lowercase (.lower()). Use a list comprehension for this.

&#x20;- Remove duplicates while keeping the original order. Loop through the cleaned list, and add an email to a new list only if it isn’t already in it.

&#x20;- Print a numbered list of the unique emails using enumerate(), starting at 1:

&#x20;  1. anna@example.com

&#x20;  2. bob@example.com

&#x20;  ...

&#x20;- Print a short report:

&#x09;How many emails you started with

&#x09;How many unique emails remain

&#x09;How many duplicates were removed

&#x20;- Count emails per domain. Every address here uses example.com, so first add a few emails with other domains (for example frank@gmail.com, grace@yahoo.com, heidi@gmail.com) to your list. Then count how many unique emails belong to each domain using .split("@") and a dictionary.



Hints:

&#x20;- " Hi ".strip().lower() gives "hi".

&#x20;- email.split("@") returns a list like \["anna", "example.com"], so the domain is the item at index 1.

&#x20;- For the dictionary count, counts\[domain] = counts.get(domain, 0) + 1 is a handy pattern.



Bonus (optional)

&#x20;- Try removing duplicates in one line using dict.fromkeys(cleaned). It keeps the order.

