EX\_29OCT - Sale Price Tag Printer

A small shop is running a sale. Items priced over 50 get a 20% discount. All other items keep their regular price.



Starting data:

&#x09;prices = \[12.50, 80.00, 45.99, 120.00, 50.00, 9.99, 65.50]



Tasks:

&#x20;- Use a list comprehension to build a new list called sale\_prices. Each item over 50 gets multiplied by 0.8, and the others stay the same. 	(Hint: you can use x \* 0.8 if x > 50 else x inside the comprehension.)

&#x20;- Use a for loop with enumerate(), starting the numbering at 1, to print each item like this:

&#x09;Item 1: 12.50 -> 12.50

&#x20;- Show both prices with 2 decimal places (for example f"{price:.2f}").

&#x20;- Add a marker (SALE!) at the end of the line for every item that was discounted.

&#x20;- After the loop, print:

&#x20;  -> how many items were discounted

&#x20;  -> the total amount saved (the sum of the original prices minus the sum of the sale prices), rounded to 2 decimals



Expected output:



Item 1: 12.50 -> 12.50

Item 2: 80.00 -> 64.00 (SALE!)

Item 3: 45.99 -> 45.99

Item 4: 120.00 -> 96.00 (SALE!)

Item 5: 50.00 -> 50.00

Item 6: 9.99 -> 9.99

Item 7: 65.50 -> 52.40 (SALE!)

Items discounted: 3

Total saved: 53.10



Bonus (optional): Let the user type the discount percentage with input() instead of hardcoding 20%.

