EX\_20JUL - Farmers Market Stand Tally

You're helping a farmers market vendor track sales across a market day.

&#x20;- Store each sale as a tuple: (item\_name, quantity, price\_per\_unit) — e.g. ("tomatoes", 3, 2.50)

&#x20;- Let the user keep entering sales until they type "done"

&#x20;- For each sale, calculate and store the total (quantity \* price\_per\_unit)

&#x20;- Use enumerate() (starting at 1) to print a numbered receipt of all sales at the end, like:

&#x20; 1. tomatoes x3 @ $2.50 = $7.50

&#x20; 2. eggs x2 @ $4.00 = $8.00

&#x20;- Use a list comprehension to calculate the grand total for the day

&#x20;- Use another list comprehension (or max() with a lambda) to find the single biggest sale (by total price)



Bonus: track how many different item types were sold, and flag if any single sale total was over $20 as a "big sale" 🎉

