EX\_11SEP - Lemonade Stand Sales Tracker

Task:

You're tracking sales for a lemonade stand over the course of a day.



&#x20;- Ask the user how many sales were made today (validate it's a positive whole number).

&#x20;- For each sale, ask for:

&#x09;Customer name

&#x09;Cup size (Small, Medium, Large) — validate against these three options, case-insensitive input is fine, but store/display it nicely capitalized

&#x09;Number of cups bought (validate it's a positive whole number)

&#x20;- Assign a price per cup based on size:

&#x09;Small = $1.50

&#x09;Medium = $2.50

&#x09;Large = $3.50

&#x20;- Store each sale as a tuple: (customer\_name, cup\_size, cups\_bought, total\_price)

&#x20;- Using enumerate() starting at 1, print a numbered summary of every sale (e.g. 1. Alice bought 2 Medium cup(s) for $5.00) — handle singular/plural for "cup(s)" correctly.

&#x20;- Print the total revenue for the day.

&#x20;- Using a list comprehension, find and print all sales where more than 2 cups were bought.

&#x20;- Using max() with a lambda, find the single biggest sale by total price (and handle ties with a list comprehension, like your usual pattern).



Bonus (optional): Build a dictionary aggregating total revenue per cup size, and print a little leaderboard sorted from highest to lowest revenue, with each size's percentage of total revenue.

